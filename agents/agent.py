from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

from config.model import azure_model
from config.notion_mcp import client
from classmodels.responsemodel import Response

async def run_agent():
    tools = await client.get_tools()
    agent = create_agent(
        tools=tools,
        model = azure_model,
        response_format=ToolStrategy(Response)
    )
    response = await agent.ainvoke({"messages": [{"role": "user", "content": "Give me a brief of my skills found in personal website page"}]})
    print(response.get("structured_response").response)
    return response