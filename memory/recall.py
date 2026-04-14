from __future__ import annotations


from .type import get_memory_root


def recall(name: str) -> str:
	memory_root = get_memory_root()
	if memory_root is None:
		raise ValueError("MEMORY_PATH is not configured.")

	memory_dir = memory_root / "memorys"
	if not memory_dir.exists():
		raise FileNotFoundError(f"Memory directory not found: {memory_dir}")

	memory_file = memory_dir / name
	if not memory_file.exists() and not memory_file.suffix:
		memory_file = memory_dir / f"{name}.md"

	if not memory_file.exists() or not memory_file.is_file():
		raise FileNotFoundError(f"No memory found for name: {name!r}")

	return memory_file.read_text(encoding="utf-8")

