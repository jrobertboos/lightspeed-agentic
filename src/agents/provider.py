from openai import AsyncOpenAI

from agents import OpenAIResponsesModel, set_default_openai_client

from src.config import Config


def configure_provider(config: Config) -> OpenAIResponsesModel:
    client = AsyncOpenAI(base_url=config.llama_stack.url, api_key="none")
    set_default_openai_client(client)
    return OpenAIResponsesModel(model="openai/gpt-4o-mini", openai_client=client)
