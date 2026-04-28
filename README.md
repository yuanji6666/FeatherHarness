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
├── FEATHER.md          # 项目描述/规范文档
├── __init__.py         # 根包初始化文件
├── client.py           # 客户端接口/通信模块
├── playground.py       # 游乐场/测试脚本
├── pyproject.toml      # Python 项目配置（依赖管理）
├── uv.lock             # uv 包管理器锁定文件
├── (.env)                # 环境变量配置
├── .env.example        # 环境变量示例
├── agent/              # Agent 核心模块目录
│   ├── __init__.py
│   ├── lead_agent.py   # 主任务代理/协调器
│   ├── subagent.py     # 子代理实现
│   └── prompt.py       # 提示词模板
├── model/              # LLM模型工厂目录
│   ├── __init__.py
│   └── factory.py      # 模型工厂类，负责创建和管理LLM实例
├── memory/             # 记忆系统模块目录
│   ├── __init__.py
│   ├── load.py         # 记忆加载器
│   ├── recall.py       # 记忆召回
│   ├── save.py         # 记忆保存
│   └── type.py         # 记忆类型定义
├── middleware/         # 中间件模块目录
│   ├── __init__.py
│   └── summarization.py # 摘要处理中间件
├── tools/              # 工具系统核心模块目录
│   ├── __init__.py
│   ├── tool.py         # 工具基类/核心实现
│   ├── builtin/        # 内置工具集合
│   │   ├── __init__.py
│   │   ├── bash_tool.py       # Bash 命令执行工具
│   │   ├── task_tool.py       # 任务分配工具
│   │   ├── web_search.py      # 网络搜索工具
│   │   ├── read_file.py       # 文件读取工具
│   │   ├── write_file.py      # 文件写入工具
│   │   ├── edit_file.py       # 文件编辑工具
│   │   ├── memory_tool.py     # 记忆工具
│   │   └── recall_tool.py     # 记忆召回工具
│   └── mcp/            # MCP 客户端模块
│       ├── __init__.py
│       └── client.py   # MCP 客户端实现
└── skill/              # Skill 加载器模块
    ├── __init__.py
    ├── skill.py        # Skill 基础定义
    └── loader.py       # Skill 加载器，实现动态加载和执行
```

### 目录说明

| 路径 | 说明 |
|------|------|
| `FEATHER.md` | 项目描述/规范文档，定义项目整体架构和技术栈 |
| `client.py` | 客户端接口/通信模块，负责与外部系统交互 |
| `playground.py` | 游乐场/测试脚本，用于调试和实验 |
| `pyproject.toml` | Python 项目配置，包含依赖管理和构建配置 |
| `.env` | 环境变量配置文件（包含敏感信息） |
| `.env.example` | 环境变量配置示例文件 |
| `agent/` | Agent 核心模块，包含主任务代理、协调器和子代理实现 |
| `model/` | LLM模型工厂，统一管理大语言模型的创建和配置 |
| `memory/` | 记忆系统模块，支持长期记忆的保存、加载和召回 |
| `middleware/` | 中间件模块，提供请求/响应的预处理和后处理功能 |
| `tools/` | 工具系统核心，提供基础功能工具集 |
| `tools/builtin/` | 内置工具集合，包括文件操作、命令行、任务分配、网络搜索和记忆管理等 |
| `tools/mcp/` | MCP 客户端模块，支持 Model Context Protocol |
| `skill/` | Skill 加载器模块，负责动态加载和执行领域特定技能 |

### MCP 服务器配置

在项目根目录创建 `mcp_servers.json` 文件，配置示例：

```json
{
  "docx": {
    "transport": "http",
    "url": "http://127.0.0.1:1314/mcp"
  }
}
```

- **键名** (`docx`): 服务器标识，可自定义
- **transport**: 传输协议，支持 `http`、`stdio` 等
- **url**: 服务器地址，本地服务格式为 `http://127.0.0.1:端口/mcp`

如需配置多个 MCP 服务器，只需在 JSON 中添加更多键值对。

### 主要特性

- **模块化设计**: 清晰的代码组织，便于维护和扩展
- **工具驱动**: 基于工具的架构，支持灵活的功能扩展
- **Agent架构**: 采用分层代理设计，支持复杂任务分解
- **LLM集成**: 统一的模型工厂，支持多种大语言模型接入
- **记忆系统**: 支持长期记忆的持久化存储和智能召回
- **MCP支持**: 集成 Model Context Protocol 协议
- **Skill系统**: 可插拔的领域能力模块，支持专业化任务处理
- **中间件支持**: 提供请求/响应的预处理和后处理管道

### 快速开始

```bash
# 激活虚拟环境
source .venv/bin/activate

# 运行 playground 测试
python playground.py
```

### 环境配置

1. 复制环境变量示例文件：
   ```bash
   cp .env.example .env
   ```

2. 编辑 `.env` 文件，配置所需的 API Key 等环境变量

3. 如需使用 MCP 服务器，配置 `mcp_servers.json`
