from fastapi import FastAPI

from app.core.config import settings
from app.health import router as health_router

def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, version="1.0.0")
    app.include_router(health_router)
    
    return app

app = create_app()