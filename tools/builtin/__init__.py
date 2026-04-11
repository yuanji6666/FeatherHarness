from .bash_tool import run_bash
from .web_search import DuckDuckGoSearchRun
from .task_tool import task_tool
from .read_file import read_file
from .edit_file import edit_file
from .write_file import write_file

builtin_tools_registry = {tool.name: tool for tool in [run_bash, DuckDuckGoSearchRun(), task_tool, read_file, edit_file, write_file]}

__all__ = [
    "builtin_tools_registry",
]