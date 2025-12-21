import os
from dotenv import load_dotenv

from langchain_openai import AzureChatOpenAI

load_dotenv()

azure_model = AzureChatOpenAI(
    model=os.getenv('AZURE_DEPLOYMENT_MODEL'),
    api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    api_version=os.getenv('AZURE_API_VERSION'),
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
    temperature=0.1
)

