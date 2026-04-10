
from agent import create_lead_agent
from langchain.agents import AgentState
from langchain.messages import HumanMessage
from dotenv import load_dotenv

import asyncio

load_dotenv()

leader = create_lead_agent()

agent_state = AgentState(messages=[])


async def main():
    while True:
        query = input("\n请输入您的问题：")
        if query.lower() in ["/bye"]:
            print("exit!")
            break
        agent_state['messages'].append(HumanMessage(content=query))

        async for chunk in leader.astream(
            input=agent_state, 
            config={"configurable":{'thread_id':1}}, 
            stream_mode='messages', 
            version='v2'
        ):
            print(chunk['data'][0].content, end='', flush=True)



if __name__ == '__main__':
    asyncio.run(main())