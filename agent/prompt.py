from xmlrpc.client import SYSTEM_ERROR

from skill import load_skill
from skill import format_skills

SYSTEM_PROMPT_TEMPLATE='''

you are a super smart agent 

# 行为指南
1.调用工具时，读写编辑等操作调用专用工具，不要调用bash_tool, bash_tool用作兜底

{skill}

'''

def get_system_prompt():
    skills = load_skill()


    return SYSTEM_PROMPT_TEMPLATE.format(skill=format_skills(skills))
    

