import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.app.endpoints import query
from src.app.state import init_app_state
from src.config import load_config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    config = load_config()
    init_app_state(config)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(query.router)


@app.get("/")
async def root():
    return {"status": "ok"}