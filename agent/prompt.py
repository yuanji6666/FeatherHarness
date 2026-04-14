from skill import load_skill
from skill import format_skills
from memory import load_memory

SYSTEM_PROMPT_TEMPLATE='''
你是轻羽智能助手FeatherAgent，你能帮用户解决长链复杂问题

# 行为指南
1.调用工具时，读写编辑等操作调用专用工具，不要调用bash_tool, bash_tool用作兜底，必须时再使用它，且必须保守使用
2.对于用户的值得长期记忆的信息或偏好，或者用户纠正你的错误，积极使用memory工具保存你的记忆,必要时可以用recall回想记忆具体内容

{memory}

{skill}

'''

def get_system_prompt():
    try:
        memory = load_memory()
    except Exception as exc:
        memory = f"记忆加载失败: {exc}"


    skills = load_skill()

    return SYSTEM_PROMPT_TEMPLATE.format(
        memory=memory,
        skill=format_skills(skills)
    )
    

