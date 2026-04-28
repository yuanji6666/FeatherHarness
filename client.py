from agent import create_lead_agent
from langchain.agents import AgentState
from langchain.messages import HumanMessage
from dotenv import load_dotenv
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

import os
import asyncio

from agent.subagent import create_sub_agent
from agent.lead_agent import get_system_prompt



agent_state = AgentState(messages=[])



async def main():
    async with AsyncPostgresSaver.from_conn_string(os.getenv("DATABASE_URL")) as memory: 
        await memory.setup()
        leader = await create_lead_agent(memory) 
        while True:
            query = input("\n请输入您的问题：")
            if query.lower() in ["/bye"]:
                print("exit!")
                break
            if query.lower() in ["/init"]:
                query = input("\n请输入你的项目开发要求：")
                init_agent = create_sub_agent(system_prompt=get_system_prompt(project_init=True))
                await init_agent.ainvoke({
                    'messages':[HumanMessage(f'用户要求:{query}')]
                })
                continue

            agent_state['messages'].append(HumanMessage(content=query))

            async for chunk in leader.astream(
                input=agent_state, 
                config={"configurable":{'thread_id':1}}, 
                stream_mode='messages', 
                version='v2'
            ):
                print(chunk['data'][0].content, end='', flush=True)



if __name__ == '__main__':
    load_dotenv()
    asyncio.run(main())