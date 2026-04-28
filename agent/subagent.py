from langchain.agents import create_agent


from model import create_chat_model

from tools import GetToolRegistery

tool_registery = GetToolRegistery()
tools = list(tool_registery.values())
def create_sub_agent(system_prompt: str):
    return create_agent(
        model=create_chat_model(),
        tools=tools,
        system_prompt=system_prompt
    )