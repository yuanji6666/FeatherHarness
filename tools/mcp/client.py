import asyncio
import json
import os

from langchain_mcp_adapters.client import MultiServerMCPClient


def _load_mcp_servers_config():
    """Load MCP servers configuration from JSON file."""
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "mcp_servers.json")
    with open(config_path, "r") as f:
        return json.load(f)


_client = None

def _get_client():
    global _client
    if _client is None:
        config = _load_mcp_servers_config()
        _client = MultiServerMCPClient(connections=config)
    return _client

_cached_tools = None

def get_mcp_tools():
    global _cached_tools
    if _cached_tools is None:
        _cached_tools = asyncio.run(_get_client().get_tools())
    return _cached_tools