from agents import Agent

from src.agents.orchestrator import OrchestratorAgent
from src.agents.provider import configure_provider
from src.agents.registry import get_agent_class
from src.config import Config


class AppState:
    def __init__(self, config: Config):
        self.config = config
        self.model = configure_provider(config)
        self.orchestrator = self._create_orchestrator()

    def _create_orchestrator(self) -> Agent:
        handoffs = []
        for agent_config in self.config.agents:
            agent_class = get_agent_class(agent_config.name)
            agent = agent_class().create(self.model)
            handoffs.append(agent)

        return OrchestratorAgent().create(self.model, handoffs=handoffs)


app_state: AppState | None = None


def init_app_state(config: Config) -> AppState:
    global app_state
    app_state = AppState(config)
    return app_state


def get_app_state() -> AppState:
    if app_state is None:
        raise RuntimeError("App state not initialized. Call init_app_state first.")
    return app_state
