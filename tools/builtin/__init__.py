from .bash_tool import run_bash
from .web_search import DuckDuckGoSearchRun
from .task_tool import task_tool   

builtin_tools_registry = {tool.name: tool for tool in [run_bash, DuckDuckGoSearchRun(), task_tool]}

__all__ = [
    "builtin_tools_registry",
]