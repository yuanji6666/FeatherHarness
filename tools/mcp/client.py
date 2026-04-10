import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.sessions import StdioConnection


_client = MultiServerMCPClient(
    connections={
        "docx": {
            'transport': 'http',
            'url':"http://127.0.0.1:1314/mcp"
        },
    }
)

_cached_tools = None

def get_mcp_tools():
    global _cached_tools
    if _cached_tools is None:
        _cached_tools = asyncio.run(_client.get_tools())
    return _cached_tools
    



                

