from pydantic import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = Path(__file__).resolve().parent.parent / ".env"  # equivale a ../.env

settings = Settings()
