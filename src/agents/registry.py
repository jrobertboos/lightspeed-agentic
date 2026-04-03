from src.agents.ansible import AnsibleAgent
from src.agents.developer_hub import DeveloperHubAgent
from src.agents.interface import AgentInterface
from src.agents.okp import OKPAgent
from src.agents.openshift import OpenShiftAgent
from src.agents.rhel import RHELAgent

AGENT_REGISTRY: dict[str, type[AgentInterface]] = {
    "okp": OKPAgent,
    "openshift": OpenShiftAgent,
    "rhel": RHELAgent,
    "ansible": AnsibleAgent,
    "developer_hub": DeveloperHubAgent,
}


def get_agent_class(name: str) -> type[AgentInterface]:
    if name not in AGENT_REGISTRY:
        raise ValueError(f"Unknown agent: {name}. Available agents: {list(AGENT_REGISTRY.keys())}")
    return AGENT_REGISTRY[name]
