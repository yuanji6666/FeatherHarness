from .builtin import get_user_info
from .builtin import run_bash

tools = [get_user_info, run_bash]

_tool_registery = {tool.name: tool for tool in tools}

def GetToolRegistery():
    return _tool_registery