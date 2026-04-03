from abc import ABC, abstractmethod
from typing import Any

from agents import Agent, OpenAIResponsesModel


class AgentInterface(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def instructions(self) -> str:
        pass

    @property
    def tools(self) -> list[Any]:
        return []

    def create(
        self,
        model: OpenAIResponsesModel,
        handoffs: list[Agent] | None = None,
    ) -> Agent:
        return Agent(
            name=self.name,
            instructions=self.instructions,
            model=model,
            tools=self.tools,
            handoffs=handoffs or [],
        )
