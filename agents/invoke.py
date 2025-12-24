import langsmith as ls
from config.config import trace_client

async def run_agent(agent, user_message):
    if agent is not None:
        config = {"configurable": {"thread_id": "1"}}
        with ls.tracing_context(client=trace_client, project_name="NotionAIze", enabled=True):
            response = await agent.ainvoke({"messages": [{"role": "user", "content": user_message}]}, config=config)
        return response.get("structured_response").response
    return None