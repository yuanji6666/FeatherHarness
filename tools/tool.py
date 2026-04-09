from langchain.tools import BaseTool

import tools

from .builtin import builtin_tools_registry


def GetToolRegistery(
        enable_task_tools = False,
):
    tool_registry = builtin_tools_registry.copy()

    if not enable_task_tools:
        tool_registry.pop('task_tool', None)
        
    return tool_registry
