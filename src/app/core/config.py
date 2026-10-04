from typing import Literal

from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    ENVIRONMENT: Literal["development", "test", "production"] = "development"
    PROJECT_NAME: str = "Boilerplate-FastAPI"
    API_V1_PREFIX: str = "/api/v1"
    DATABASE_URL: str
    
settings = Settings() # pyright: ignore[reportCallIssue]