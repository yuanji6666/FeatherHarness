# Project: FeatherHarness
一句话项目定位与核心目标：一个基于 LangChain & LangGraph 的 AI Agent 运行时 Harness（驾驭系统），通过状态机编排和环境层释放 LLM 的最大能力

## About This Project
项目简介：FeatherHarness 是一个 AI Agent 运行时框架，采用 LangGraph 状态机进行工作流编排。核心思想是将 LLM 看作一匹奔腾的马，而 Harness（马具/环境层）是保证其能力能最高效释放的外在系统。项目支持工具驱动架构、分层代理设计、MCP 协议集成以及可插拔的 Skill 系统，可用于复杂任务的分解与执行。

## Tech Stack
- 语言：Python >= 3.14
- 框架：LangChain, LangGraph
- 数据库/ORM：langgraph-checkpoint-postgres（用于状态持久化）
- 工具链：uv（项目依赖管理）, IPython（交互式开发）
- LLM：OpenAI

## Key Directories
- `agent/` - Agent 核心模块，包含主任务代理和协调逻辑
- `model/` - LLM 模型工厂，统一管理大语言模型的创建和配置
- `subagent/` - 子代理模块，处理具体的任务执行和分解
- `middleware/` - 中间件模块，提供请求/响应的预处理和后处理功能
- `tools/` - 工具系统核心，提供基础功能工具集
- `tools/builtin/` - 内置工具集合（bash, task_tool, web_search 等）
- `tools/mcp/` - MCP 客户端模块，支持 Model Context Protocol
- `skill/` - Skill 加载器模块，负责动态加载和执行技能
- `skills/` - Skill 集合目录，包含可复用的技能模块
- `memory/` - 记忆模块（save/recall/load）
- ⚠️ `.venv/` - 禁止修改、只读目录（虚拟环境）

## Common Commands
```bash
# 安装依赖（使用 uv）
uv sync

# 进入虚拟环境
source .venv/bin/activate

# 运行 playground 测试
python playground.py

# 更新依赖
uv lock --upgrade
```
