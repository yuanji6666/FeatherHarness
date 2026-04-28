from langchain.tools import tool
from langchain.messages import HumanMessage


@tool("task_tool", description="a tool to assign task to subagent")
def task_tool(task_description: str):
    from agent import create_sub_agent 
    subagent = create_sub_agent("you are a smart agent")
    result = subagent.invoke({
        'messages': [HumanMessage(content=task_description)],
    })

    return result['messages'][-1].content




    