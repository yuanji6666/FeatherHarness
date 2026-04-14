from __future__ import annotations

import os
from pathlib import Path


MEMORY_TYPE = ("user", "feedback")


def get_memory_root() -> Path | None:
	memory_path = os.environ.get("MEMORY_PATH")
	if not memory_path:
		return None
	return Path(memory_path).expanduser()

