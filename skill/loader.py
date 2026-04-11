import os
import re
from pathlib import Path

from .skill import Skill

_skills_path = Path(os.environ.get("SKILL_PATH") or './skills')


def load_skill():
    skills: list[Skill] = []
    if not _skills_path.exists() or not _skills_path.is_dir():
        return skills

    for path in _skills_path.iterdir():
        if not path.is_dir():
            continue

        skill_file_path = path / "SKILL.md"
        if not skill_file_path.exists():
            continue

        skill = _parse_skill_file(skill_file_path)
        if skill is not None:
            skills.append(skill)

    return skills


def _parse_skill_file(skill_file_path: Path) -> Skill | None:
    content = skill_file_path.read_text(encoding="utf-8")

    # Match YAML front matter at the beginning of the file.
    front_matter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not front_matter_match:
        return None

    front_matter = front_matter_match.group(1)
    metadata: dict[str, str] = {}

    lines = front_matter.split("\n")
    current_key = None
    current_value: list[str] = []
    is_multiline = False
    multiline_style = None
    indent_level = None

    for line in lines:
        if is_multiline:
            if not line.strip():
                current_value.append("")
                continue

            current_indent = len(line) - len(line.lstrip())

            if indent_level is None:
                if current_indent > 0:
                    indent_level = current_indent
                    current_value.append(line[indent_level:])
                    continue
            elif current_indent >= indent_level:
                current_value.append(line[indent_level:])
                continue

        if current_key and is_multiline:
            if multiline_style == "|":
                metadata[current_key] = "\n".join(current_value).rstrip()
            else:
                text = "\n".join(current_value).rstrip()
                metadata[current_key] = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

            current_key = None
            current_value = []
            is_multiline = False
            multiline_style = None
            indent_level = None

        if not line.strip():
            continue

        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if value in (">", "|"):
                current_key = key
                is_multiline = True
                multiline_style = value
                current_value = []
                indent_level = None
            else:
                metadata[key] = value

    if current_key and is_multiline:
        if multiline_style == "|":
            metadata[current_key] = "\n".join(current_value).rstrip()
        else:
            text = "\n".join(current_value).rstrip()
            metadata[current_key] = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

    name = metadata.get("name")
    description = metadata.get("description")
    if not name or not description:
        return None

    return Skill(
        name=name,
        description=description,
        dir_path=skill_file_path.parent,
        file_path=skill_file_path,
    )

