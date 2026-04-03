import uvicorn

from src.config import Config


def run(config: Config):
    uvicorn.run(
        "src.app.main:app",
        host=config.service.host,
        port=config.service.port,
        reload=True,
    )
