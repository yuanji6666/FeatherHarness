from langchain.agents import create_agent


from model import create_chat_model

from tools import GetToolRegistery

tool_registery = GetToolRegistery()
tools = list(tool_registery.values())
def get_subagent():
    return create_agent(
        model=create_chat_model(),
        tools=tools,
    )