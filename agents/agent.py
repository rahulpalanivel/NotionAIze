from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langgraph.checkpoint.memory import InMemorySaver


from config.config import azure_model
from config.notion_mcp import client
from classmodels.responsemodel import Response
from prompts.prompt import SYSTEM_PROMPT
from config.config import trace_client, memory

async def create_notion_agent():
    tools = await client.get_tools()
    agent = create_agent(
            system_prompt=SYSTEM_PROMPT,
            checkpointer=memory,
            tools=tools,
            model = azure_model,
            response_format=ToolStrategy(Response)
        )
    return agent



