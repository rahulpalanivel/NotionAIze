import os
from dotenv import load_dotenv

import langsmith as ls
from langchain_openai import AzureChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

azure_model = AzureChatOpenAI(
    model=os.getenv('AZURE_DEPLOYMENT_MODEL'),
    api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    api_version=os.getenv('AZURE_API_VERSION'),
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
    temperature=0.1
)


trace_client = ls.Client(
    api_url="https://api.smith.langchain.com",
    api_key=os.getenv("TRACING_KEY")
)

memory = InMemorySaver()
