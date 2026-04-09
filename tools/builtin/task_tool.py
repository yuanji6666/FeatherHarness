from langchain.tools import tool
from langchain.messages import HumanMessage


@tool("task_tool", description="a tool to assign task to subagent")
def task_tool(task_description: str):
    from subagent import get_subagent
    subagent = get_subagent()
    result = subagent.invoke({
        'messages': [HumanMessage(content=task_description)],
        'turn_count': 0
    })

    return result['messages'][-1].content




    