import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage, ToolMessage
from dotenv import load_dotenv
import os

load_dotenv()

class State(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    turn_count: int
    transition_reason: str

graph = StateGraph(State)

chatModel = ChatOpenAI(base_url=os.getenv("OPENAI_BASE_URL") or "https://api.qnaigc.com/v1",
                    model=os.getenv("OPENAI_MODEL_NAME") or "z-ai/glm-5")


@tool
def get_user_info() -> str:
    """这个工具可以用来获得用户的个人信息
    """
    return "我叫小源，今年19岁，在武汉大学大学计算机学院读大二"

tools = [get_user_info]

tool_registery = {tool.name: tool for tool in tools}

def llm_call(state: State):
    model = chatModel.bind_tools([get_user_info])
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
    from IPython.display import Image, display
    display(Image(agent.get_graph(xray=True).draw_mermaid_png()))
    
    state = agent.invoke(State(messages=[HumanMessage(content='你知道我多少岁吗？')], turn_count=0, transition_reason=''))

    for m in state['messages']:
        m.pretty_print()






