from skill import load_skill
from skill import format_skills

SYSTEM_PROMPT_TEMPLATE='''
You are FeatherAgent, An intelligent assistant that can solve all kinds of problems.

# 行为指南
1.调用工具时，读写编辑等操作调用专用工具，不要调用bash_tool, bash_tool用作兜底，必须时再使用它，且必须保守使用

{skill}

'''

def get_system_prompt():

    skills = load_skill()

    return SYSTEM_PROMPT_TEMPLATE.format(skill=format_skills(skills))
    

