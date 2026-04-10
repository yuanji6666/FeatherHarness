from .builtin import builtin_tools_registry
from tools.mcp import get_mcp_tools 


def GetToolRegistery(
        enable_task_tools = False,
):
    tool_registry = builtin_tools_registry.copy()

    if not enable_task_tools:
        tool_registry.pop('task_tool', None)
        
    tools = get_mcp_tools()
    print(f"avaiable mcp tools : {len(tools)}")
    
    tool_registry = {**tool_registry, **{tool.name : tool for tool in tools}}
        
    return tool_registry
