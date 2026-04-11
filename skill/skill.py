from pathlib import Path

from attr import dataclass


@dataclass
class Skill:
    name: str
    description: str
    dir_path: Path
    file_path: Path

def format_skills(skills: list[Skill]):
    format_string = "# 可用skill\n"
    for i, skill in enumerate(skills, 1):
        format_string += f"{i}. {skill.name}\n"
        format_string += f"   描述: {skill.description}\n"
        format_string += f"   目录: {skill.dir_path}\n"
        format_string += f"   文件: {skill.file_path}\n"
    return format_string