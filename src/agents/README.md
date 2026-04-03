# Agents

This directory contains the agent implementations for the Lightspeed Agentic system.

## Creating a Custom Agent

All agents must implement the `AgentInterface` abstract base class.

### 1. Create a new agent file

Create a new file in `src/agents/` (e.g., `my_agent.py`):

```python
from agents import function_tool

from src.agents.interface import AgentInterface


@function_tool
def my_tool(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"


class MyAgent(AgentInterface):
    @property
    def name(self) -> str:
        return "MyAgent"

    @property
    def instructions(self) -> str:
        return """Your agent instructions here.

Describe what this agent does and how it should behave.
"""

    @property
    def tools(self) -> list:
        return [my_tool]
```

### 2. Export the agent

Add your agent to `src/agents/__init__.py`:

```python
from src.agents.my_agent import MyAgent

__all__ = [..., "MyAgent"]
```

### 3. Use your agent

```python
from src.config import load_config
from src.agents import configure_provider, MyAgent

config = load_config()
model = configure_provider(config)

agent = MyAgent().create(model)
```

## Agent Interface

The `AgentInterface` requires two properties and has one optional property:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `str` | Yes | The display name of the agent |
| `instructions` | `str` | Yes | System prompt defining the agent's behavior |
| `tools` | `list` | No | List of tools available to the agent (default: `[]`) |

The interface provides a `create(model)` method that returns a configured `Agent` instance using the OpenAI Agents SDK.

## Adding Tools

Tools can be added by overriding the `tools` property. Use the `@function_tool` decorator from the OpenAI Agents SDK:

```python
from agents import function_tool


@function_tool
def search_knowledge_base(query: str) -> str:
    """Search the knowledge base for relevant information."""
    # Implementation here
    return results
```

Then include the tool in your agent's `tools` property.

## Existing Agents

- **OrchestratorAgent** - Coordinates tasks and delegates work to specialized agents
- **OKPAgent** - RAG agent for retrieving and synthesizing information from a knowledge base
