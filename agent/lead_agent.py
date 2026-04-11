from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

from model.factory import create_chat_model
from tools import GetToolRegistery

from .prompt import get_system_prompt
def create_lead_agent():
    memory = MemorySaver()
    leader = create_agent(
        model = create_chat_model(),
        tools = [tool for tool in GetToolRegistery(enable_task_tools=True).values()],     
        checkpointer=memory,
        system_prompt=get_system_prompt()
    )
    
    return leader

