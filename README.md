# FeatherHarness

### 技术栈

基于 LangChain & LangGraph

其实LangGraph的状态机编排逻辑非常巧妙

### Harness—驾驭系统

> $Agent = Loop(LLM + Harness)$

最近Harness这个词很火，在我看来它不算是什么新概念，但是确实是Agent工程的一个很形象凝练的概括，是对过去所做的Agent工程的一个总结

Harness有（马的）挽具，马具的意思，可以把LLM看作系统中一匹奔腾的马，能力强大，但是需要一层外在环境，保证它的能力能够最高效地释放出来

这个Agent运行时的工作环境，就是Harness，是Agent工程关注的核心


## 项目结构

```
├── README.md           # 项目说明文档
├── __init__.py         # 根包初始化文件
├── client.py           # 客户端接口/通信模块
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
└── tools/              # 工具系统核心模块目录
    ├── __init__.py     # tool 包初始化
    ├── tool.py         # 工具基类/核心实现
    └── builtin/        # 内置工具集合
        ├── __init__.py # builtin 包初始化
        ├── bash_tool.py    # Bash 命令执行工具
        ├── task_tool.py    # 任务分配工具
        └── web_search.py   # 网络搜索工具
```

### 目录说明

| 路径 | 说明 |
|------|------|
| `client.py` | 客户端接口/通信模块，负责与外部系统交互 |
| `agent/` | Agent 核心模块，包含主任务代理和协调逻辑 |
| `model/` | LLM模型工厂，统一管理大语言模型的创建和配置 |
| `subagent/` | 子代理模块，处理具体的任务执行和分解 |
| `tools/` | 工具系统核心，提供基础功能工具集 |
| `tools/builtin/` | 内置工具集合，包括命令行、任务分配和网络搜索等基础功能 |

### 主要特性

- **模块化设计**: 清晰的代码组织，便于维护和扩展
- **工具驱动**: 基于工具的架构，支持灵活的功能扩展
- **Agent架构**: 采用分层代理设计，支持复杂任务分解
- **LLM集成**: 统一的模型工厂，支持多种大语言模型接入
- **环境隔离**: 使用 .venv 虚拟环境，保证依赖管理清晰

