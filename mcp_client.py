from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import AzureChatOpenAI
from langchain.agents.structured_output import ToolStrategy
from pydantic import BaseModel

import os
from dotenv import load_dotenv

load_dotenv() 

TOKEN = os.getenv("NOTION_MCP_TOKEN")

class Response(BaseModel):
    """Class to define the response schema."""
    response:str

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

azure_model = AzureChatOpenAI(
    model=os.getenv('AZURE_DEPLOYMENT_MODEL'),
    api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    api_version=os.getenv('AZURE_API_VERSION'),
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
    temperature=0.1
)

async def run_agent():
    tools = await client.get_tools()
    agent = create_agent(
        tools=tools,
        model = azure_model,
        response_format=ToolStrategy(Response)
    )
    response = await agent.ainvoke({"messages": [{"role": "user", "content": "Give me a brief of my education found in personal website page"}]})
    print(response.get("structured_response").response)


if __name__ == "__main__":
    import asyncio
    asyncio.run(run_agent())