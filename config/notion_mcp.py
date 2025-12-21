import os
from dotenv import load_dotenv

from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv() 

TOKEN = os.getenv("NOTION_MCP_TOKEN")
client = MultiServerMCPClient(
    {
        "notion": {
            "transport": "http",
            "url": "http://localhost:3000/mcp",
            "headers":{
                "Authorization": f"Bearer {TOKEN}",
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream"
            }
        }
    }
)