from .builtin import get_user_info
from .builtin import run_bash
from .builtin import DuckDuckGoSearchRun

tools = [get_user_info, run_bash, DuckDuckGoSearchRun()]

_tool_registery = {tool.name: tool for tool in tools}

def GetToolRegistery():
    return _tool_registery