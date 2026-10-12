from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.db.session import engine
from app.health import router as health_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    yield  # aqui o app roda
    await engine.dispose()  # shutdown: fecha o pool de conexões


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, version="1.0.0", lifespan=lifespan)
    app.include_router(health_router)
    return app


app = create_app()