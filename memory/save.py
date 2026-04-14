from __future__ import annotations

import re

from .type import MEMORY_TYPE, get_memory_root


def _sanitize_filename(name: str) -> str:
	sanitized = re.sub(r"[^A-Za-z0-9._-]+", "_", name.strip())
	sanitized = sanitized.strip("._-")
	return sanitized or "memory"


def save_memory(name: str, description: str, type: str, content: str) -> str:
	if type not in MEMORY_TYPE:
		raise ValueError(f"Invalid memory type: {type!r}. Expected one of {MEMORY_TYPE!r}.")

	memory_root = get_memory_root()
	if memory_root is None:
		raise ValueError("MEMORY_PATH is not configured.")

	memory_dir = memory_root / "memorys"
	memory_dir.mkdir(parents=True, exist_ok=True)

	filename = f"{_sanitize_filename(name)}.md"
	memory_file = memory_dir / filename


	frontmatter = [
		"---",
		f"name: {name}",
		f"description: {description}",
		f"type: {type}",
		"---",
		"",
	]
	memory_block = "\n".join(frontmatter) + f"{content}\n"
	if memory_file.exists():
		existing = memory_file.read_text(encoding="utf-8")
		if existing and not existing.endswith("\n"):
			existing += "\n"
		memory_file.write_text(existing + "\n" + memory_block, encoding="utf-8")
	else:
		memory_file.write_text(memory_block, encoding="utf-8")

	index_file = memory_root / "MEMORY.md"
	index_line = f"- [{type}]{name} - {description}".rstrip()
	if index_file.exists():
		existing = index_file.read_text(encoding="utf-8")
		if existing and not existing.endswith("\n"):
			existing += "\n"
		if index_line not in existing:
			existing += index_line + "\n"
		index_file.write_text(existing, encoding="utf-8")
	else:
		index_file.write_text(f"# Memory Index\n\n{index_line}\n", encoding="utf-8")

	return str(memory_file)
