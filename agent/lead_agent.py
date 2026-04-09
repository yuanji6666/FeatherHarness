from typing import Any

from langchain.agents import create_agent
from langchain.messages import HumanMessage
from pathlib import Path

from model.factory import create_chat_model
from tools import GetToolRegistery

leader = create_agent(
    model = create_chat_model(),
    tools = [tool for tool in GetToolRegistery(enable_task_tools=True).values()]     
)

if __name__ == "__main__":
    png = leader.get_graph().draw_mermaid_png()
    Path("lead_agent_graph.png").write_bytes(png)


    agent_state: Any = {"messages": []}
    while True:
        query = input("请输入您的问题：")
        if query.lower() in ["exit", "quit"]:
            print("退出程序。")
            break
        agent_state['messages'].append(HumanMessage(content=query))
        agent_state = leader.invoke(agent_state)
    

    for m in agent_state['messages']:
        m.pretty_print()
