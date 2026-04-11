# FeatherHarness

### 一点感想

一边做这个项目一边调试，仅仅是给agent加了一个bash_tool放进一个简单的Loop，它就能分析整个项目并完成任务了，甚至可以开始自己写自己

再次感慨AI的强大

### 技术栈

基于 LangChain & LangGraph

其实LangGraph的状态机编排逻辑非常巧妙

### Harness—驾驭系统

> $Agent = Loop(LLM + Harness)$

最近Harness这个词很火，在我看来它不算是什么新概念，但是确实是Agent工程的一个很形象凝练的概括，是对过去所做的Agent工程的一个总结

Harness有（马的）挽具，马具的意思，可以把LLM看作系统中一匹奔腾的马，能力强大，但是需要一层外在环境，保证它的能力能够最高效地释放出来

这个Agent运行时的工作环境，就是Harness，是Agent工程关注的核心


### 项目架构

```
├── README.md           # 项目说明文档
├── __init__.py         # 根包初始化文件
├── client.py           # 客户端接口/通信模块
├── playground.py       # 游乐场/测试脚本
├── pyproject.toml      # Python 项目配置（依赖管理）
├── uv.lock             # uv 包管理器锁定文件
├── agent/              # Agent 核心模块目录
│   ├── __init__.py     # agent 包初始化
│   └── lead_agent.py   # 主任务代理/协调器
├── model/              # LLM模型工厂目录
│   ├── __init__.py     # model 包初始化
│   └── factory.py      # 模型工厂类，负责创建和管理LLM实例
├── subagent/           # 子代理模块目录
│   ├── __init__.py     # subagent 包初始化
│   └── subagent.py     # 子代理实现，处理具体任务执行
├── tools/              # 工具系统核心模块目录
│   ├── __init__.py     # tool 包初始化
│   ├── tool.py         # 工具基类/核心实现
│   ├── builtin/        # 内置工具集合
│   │   ├── __init__.py # builtin 包初始化
│   │   ├── bash_tool.py    # Bash 命令执行工具
│   │   ├── task_tool.py    # 任务分配工具
│   │   └── web_search.py   # 网络搜索工具
│   └── mcp/            # MCP 客户端模块
│       ├── __init__.py # mcp 包初始化
│       └── client.py   # MCP 客户端实现
├── skill/              # Skill 加载器模块
│   ├── __init__.py     # skill 包初始化
│   ├── skill.py        # Skill 基础定义
│   └── loader.py       # Skill 加载器，实现动态加载和执行
└── skills/             # Skill 集合目录
    └── academic-paper-review/  # 学术论文审查技能
        └── SKILL.md    # Skill 定义文件
```

### 目录说明

| 路径 | 说明 |
|------|------|
| `client.py` | 客户端接口/通信模块，负责与外部系统交互 |
| `playground.py` | 游乐场/测试脚本，用于调试和实验 |
| `agent/` | Agent 核心模块，包含主任务代理和协调逻辑 |
| `model/` | LLM模型工厂，统一管理大语言模型的创建和配置 |
| `subagent/` | 子代理模块，处理具体的任务执行和分解 |
| `tools/` | 工具系统核心，提供基础功能工具集 |
| `tools/builtin/` | 内置工具集合，包括命令行、任务分配和网络搜索等基础功能 |
| `tools/mcp/` | MCP 客户端模块，支持 Model Context Protocol |
| `skill/` | Skill 加载器模块，负责动态加载和执行技能 |
| `skills/` | Skill 集合目录，包含可复用的技能模块 |

### 主要特性

- **模块化设计**: 清晰的代码组织，便于维护和扩展
- **工具驱动**: 基于工具的架构，支持灵活的功能扩展
- **Agent架构**: 采用分层代理设计，支持复杂任务分解
- **LLM集成**: 统一的模型工厂，支持多种大语言模型接入
- **环境隔离**: 使用 .venv 虚拟环境，保证依赖管理清晰
- **MCP支持**: 集成 Model Context Protocol 协议
- **Skill系统**: 可插拔的领域能力模块，支持专业化任务处理