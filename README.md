# FeatherHarness

### 技术栈

基于 LangChain & LangGraph

其实LangGraph的状态机编排逻辑非常巧妙

### Harness—驾驭系统

> $Agent = Loop(LLM + Harness)$

最近Harness这个词很火，在我看来它不算是什么新概念，但是确实是Agent工程的一个很形象凝练的概括，是对过去所做的Agent工程的一个总结

Harness有（马的）挽具，马具的意思，可以把LLM看作系统中一匹奔腾的马，能力强大，但是需要一层外在环境，保证它的能力能够最高效地释放出来

这个Agent运行时的工作环境，就是Harness，是Agent工程关注的核心

---

## 项目结构

```
.
├── README.md           # 项目说明文档
├── __init__.py         # 根包初始化文件
├── main.py             # 程序入口/主文件
├── pyproject.toml      # Python 项目配置（依赖管理）
├── uv.lock             # uv 包管理器锁定文件
├── tool/               # 工具模块目录
│   ├── __init__.py     # tool 包初始化
│   ├── tool.py         # 工具基类/核心实现
│   └── builtin/        # 内置工具集合
│       ├── __init__.py # builtin 包初始化
│       ├── bash_tool.py    # Bash 命令执行工具
│       └── get_user_info.py # 用户信息获取工具
```

### 目录说明

| 路径 | 说明 |
|------|------|
| `main.py` | Agent 程序入口，负责编排整体流程 |
| `tool/` | 工具系统核心模块，定义工具接口和注册机制 |
| `tool/tool.py` | 工具基类，所有工具需要继承实现 |
| `tool/builtin/` | 系统内置的基础工具 |
| `tool/builtin/bash_tool.py` | 提供执行 Bash 命令的能力 |
| `tool/builtin/get_user_info.py` | 提供获取用户信息的功能 |
