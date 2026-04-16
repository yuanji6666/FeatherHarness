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

def get_project_analysis():
    cwd_path = Path.cwd()
    file = cwd_path / "FEATHER.md"
    if not file.exists():
        return "" 
    return "# 当前项目描述 (FEATHER.md) \n" + file.read_text()
    


def get_system_prompt():

    try:
        memory = load_memory()
    except Exception as exc:
        memory = f"记忆加载失败: {exc}"


    skills = load_skill()

    return SYSTEM_PROMPT_TEMPLATE.format(
        project= get_project_analysis(),
        memory=memory,
        skill=format_skills(skills)
    )
    
if __name__ == "__main__":
    print(get_project_analysis())
    

