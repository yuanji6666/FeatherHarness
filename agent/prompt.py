from skill import load_skill
from skill import format_skills
from memory import load_memory
from pathlib import Path

SYSTEM_PROMPT_TEMPLATE='''
你是轻羽智能助手FeatherAgent，你能帮用户解决长链复杂问题

# 行为指南
1.调用工具时，读写编辑等操作调用专用工具，不要调用bash_tool, bash_tool用作兜底，必须时再使用它，且必须保守使用
2.对于用户的值得长期记忆的信息或偏好，或者用户纠正你的错误，积极使用memory工具保存你的记忆,必要时可以用recall回想记忆具体内容
3.当前项目描述保存在项目根目录FEATHER.md, 它会在下面的“当前项目描述”中显示，每当你对项目整体架构或技术栈做了修改时，调用工具更新FEATHER.md

{project}

{memory}

{skill}

'''

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

def _get_project_analysis():
    cwd_path = Path.cwd()
    file = cwd_path / "FEATHER.md"
    if not file.exists():
        return "" 
    return "# 当前项目描述 (FEATHER.md) \n" + file.read_text()
    


def get_system_prompt(
        project_init: bool | None = False,
        include_project_introdution: bool = False,
        include_memory: bool | None = False,
        include_skills: bool | None = False,
):
    
    if project_init:
        return PROJECT_INIT_PROMPT
    
    project_analysis = _get_project_analysis() if include_project_introdution else ""
    memory = load_memory() if include_memory else ""
    skills = load_skill() if include_skills else []

    return SYSTEM_PROMPT_TEMPLATE.format(
        project= project_analysis,
        memory=memory,
        skill=format_skills(skills)
    )
    
    