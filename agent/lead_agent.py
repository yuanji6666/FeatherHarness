from langchain.agents import create_agent

from middleware.summarization import get_summarization_middleware
from model.factory import create_chat_model
from tools import GetToolRegistery

from .prompt import get_system_prompt
async def create_lead_agent(memory):
        leader = create_agent(
            model = create_chat_model(),
            tools = [tool for tool in GetToolRegistery(enable_task_tools=True).values()],     
            checkpointer=memory,
            system_prompt=get_system_prompt(),
            middleware=[get_summarization_middleware()]
        )
        
        return leader

