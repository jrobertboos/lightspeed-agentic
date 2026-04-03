from agents import Runner
from fastapi import APIRouter
from pydantic import BaseModel

from src.agents.hooks import LoggingHooks
from src.app.state import get_app_state

router = APIRouter()


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    result: str


@router.post("/query")
async def query(request: QueryRequest) -> QueryResponse:
    state = get_app_state()
    result = await Runner.run(
        state.orchestrator,
        request.query,
        hooks=LoggingHooks(),
    )
    return QueryResponse(result=result.final_output)
