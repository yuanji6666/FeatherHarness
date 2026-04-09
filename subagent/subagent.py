from langchain.messages import AnyMessage, HumanMessage, SystemMessage, ToolMessage, AIMessage
from langgraph.graph import END, START, StateGraph

from model import create_chat_model

from typing import Annotated, TypedDict
import operator


class SubAgentState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    turn_count: int

graph = StateGraph(SubAgentState)

from tools import GetToolRegistery

tool_registery = GetToolRegistery()
tools = list(tool_registery.values())


chatModel = create_chat_model()
def llm_call(state: SubAgentState):
    model = chatModel.bind_tools(tools)
    AImessage = model.invoke(input=
        [SystemMessage("you are a smart agent with tool calling ability,you should compelete the tasks assigned to you")]+state['messages']
        )

    AImessage.pretty_print()
    
    return {
        'messages': [AImessage],
        'turn_count': state['turn_count']+1,
        'transition_reason': 'tool_call'
    }


def tool_node(state: SubAgentState):
    result = []
    
    lastMessage = state['messages'][-1]
    
    if isinstance(lastMessage, AIMessage):
        for tool_call in lastMessage.tool_calls:
            if tool_call['name'] in tool_registery:
                tool = tool_registery[tool_call['name']]
                observation = tool.invoke(tool_call["args"])
                tool_message = ToolMessage(content=observation, tool_call_id=tool_call['id'])
                tool_message.pretty_print()
                result.append(tool_message)


    return {"messages": result}

def should_continue(state: SubAgentState):
    lastMessage = state['messages'][-1]

    if not isinstance(lastMessage, AIMessage):
        raise ValueError

    if len(lastMessage.tool_calls) != 0:
        return "tool_node"

    return END

graph.add_node('llm_call', llm_call)
graph.add_node('tool_node', tool_node)

graph.add_edge(START, 'llm_call')
graph.add_conditional_edges(
    'llm_call',
    should_continue,
    ['tool_node', END]
)
graph.add_edge('tool_node', 'llm_call')

_subagent = graph.compile()


def get_subagent():
    return _subagent