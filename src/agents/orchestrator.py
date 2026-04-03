from src.agents.interface import AgentInterface


class OrchestratorAgent(AgentInterface):
    @property
    def name(self) -> str:
        return "Orchestrator"

    @property
    def instructions(self) -> str:
        return """You are an orchestrator agent responsible for coordinating tasks and delegating work to specialized agents.

Your responsibilities:
- Analyze incoming requests and determine the best approach
- Break down complex tasks into smaller subtasks
- Delegate work to appropriate specialized agents
- Synthesize results from multiple agents into coherent responses
- Handle errors and retry logic when needed
"""
