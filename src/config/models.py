from typing import Any

from pydantic import BaseModel


class ServiceConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class LlamaStackConfig(BaseModel):
    url: str


class AgentConfig(BaseModel):
    name: str
    config: dict[str, Any] = {}


class Config(BaseModel):
    name: str
    service: ServiceConfig
    llama_stack: LlamaStackConfig
    agents: list[AgentConfig] = []
