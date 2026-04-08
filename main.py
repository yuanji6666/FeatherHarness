import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph
from langchain_openai import ChatOpenAI
from langchain.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage, ToolMessage
from dotenv import load_dotenv
import os

from tool import GetToolRegistery

load_dotenv()

class State(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    turn_count: int
    transition_reason: str

graph = StateGraph(State)

chatModel = ChatOpenAI(base_url=os.getenv("OPENAI_BASE_URL") or "https://api.qnaigc.com/v1",
                    model=os.getenv("OPENAI_MODEL_NAME") or "z-ai/glm-5")

tool_registery = GetToolRegistery()
tools = [tool_ for tool_ in tool_registery.values()]
def llm_call(state: State):
    model = chatModel.bind_tools(tools)
    AImessage = model.invoke([SystemMessage("你是一个可以调用工具的智能助手，如果需要工具，请调用")]+state['messages'])

    AImessage.pretty_print()
    
    return {
        'messages': [AImessage],
        'turn_count': state['turn_count']+1,
        'transition_reason': 'tool_call'
    }


def tool_node(state: State):
    result = []
    
    lastMessage = state['messages'][-1]
    
    if isinstance(lastMessage, AIMessage):
        for tool_call in lastMessage.tool_calls:
            if tool_call['name'] in tool_registery:
                tool = tool_registery[tool_call['name']]
                observation = tool.invoke(tool_call["args"])
                result.append(ToolMessage(content=observation, tool_call_id=tool_call['id']))

    return {"messages": result}

def should_continue(state: State):
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

agent = graph.compile()

if __name__ == '__main__':
    userInput = input("请输入问题：")

    state = agent.invoke(State(messages=[HumanMessage(content=userInput)], turn_count=0, transition_reason=''))

    for m in state['messages']:
        m.pretty_print()






