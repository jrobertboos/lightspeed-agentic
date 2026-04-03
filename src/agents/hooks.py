import logging
from typing import Any

from agents import Agent, RunContextWrapper, RunHooks, Tool

logger = logging.getLogger(__name__)


class LoggingHooks(RunHooks):
    async def on_agent_start(
        self,
        context: RunContextWrapper,
        agent: Agent,
    ) -> None:
        logger.info(f"Agent started: {agent.name}")

    async def on_agent_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        output: str,
    ) -> None:
        logger.info(f"Agent ended: {agent.name}")
        logger.info(f"Agent output: {output}")

    async def on_handoff(
        self,
        context: RunContextWrapper,
        from_agent: Agent,
        to_agent: Agent,
    ) -> None:
        logger.info(f"Handoff: {from_agent.name} -> {to_agent.name}")

    async def on_tool_start(
        self,
        context: RunContextWrapper,
        agent: Agent,
        tool: Tool,
    ) -> None:
        logger.info(f"Tool started: {tool.name} (agent: {agent.name})")

    async def on_tool_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        tool: Tool,
        result: Any,
    ) -> None:
        logger.info(f"Tool ended: {tool.name} (agent: {agent.name})")
        logger.info(f"Tool result: {result}")
