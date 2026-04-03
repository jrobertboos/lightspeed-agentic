from src.agents.interface import AgentInterface


class OKPAgent(AgentInterface):
    @property
    def name(self) -> str:
        return "OKP"

    @property
    def instructions(self) -> str:
        return """You are a RAG (Retrieval-Augmented Generation) agent responsible for retrieving relevant information and generating accurate responses.

Your responsibilities:
- Search and retrieve relevant documents from the knowledge base
- Synthesize retrieved information into accurate, contextual responses
- Cite sources when providing information
- Handle cases where information is not found gracefully
"""
