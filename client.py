from agent import create_lead_agent
from langchain.agents import AgentState
from langchain.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

leader = create_lead_agent()

agent_state = AgentState(messages=[])

while True:
    query = input("请输入您的问题：")
    if query.lower() in ["/bye"]:
        print("exit!")
        break
    agent_state['messages'].append(HumanMessage(content=query))
    for chunk in leader.stream(agent_state,config={"configurable":{'thread_id':1}}, stream_mode="updates"):
        for node, output in chunk.items():
            print(output['messages'][-1].pretty_print())

for m in agent_state['messages']:
    m.pretty_print()