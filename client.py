from agent import create_lead_agent
from langchain.agents import AgentState
from langchain.messages import HumanMessage
from dotenv import load_dotenv
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

import os
import asyncio

from subagent.subagent import get_subagent



agent_state = AgentState(messages=[])

PROJECT_INIT_PROMPT = '''
你是一个项目分析智能体，职责是根据用户需要分析整个项目，让之后智能体对项目架构可以一目了然

把分析文件写成“FEATHER.md”存在当前项目根目录之下

请认真关注用户描述！

你输出的格式应该是：

# Project: [项目名称]
一句话项目定位与核心目标（官方默认开头）

## About This Project
项目简介：做什么、核心价值、业务场景、当前状态

## Tech Stack
- 语言：[如 Python 3.11, TypeScript 5.4]
- 框架：[如 FastAPI, Next.js 14 App Router]
- 数据库/ORM：[如 PostgreSQL + SQLAlchemy]
- 工具链：[如 pnpm, pytest, ESLint, Prettier]

## Key Directories
- `src/` - 主源码目录
- `src/api/` - 接口路由
- `src/core/` - 核心逻辑/配置
- `tests/` - 测试用例
- `scripts/` - 构建/部署脚本
- 标注：⚠️ 禁止修改、只读目录

## Common Commands
```bash
# 开发启动
pnpm dev
# 生产构建
pnpm build
# 运行测试
pytest tests/ -v
# 代码检查
pnpm lint

'''


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
                init_agent = get_subagent(system_prompt=PROJECT_INIT_PROMPT)
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