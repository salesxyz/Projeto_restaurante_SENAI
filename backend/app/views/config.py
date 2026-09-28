"""Configurações centrais da aplicação, lidas de variáveis de ambiente."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "SALES3DS API"
    API_V1_PREFIX: str = "/api/v1"

    DATABASE_URL: str = "sqlite:///./sales3ds.db"

    SECRET_KEY: str = "change-me-in-.env"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
