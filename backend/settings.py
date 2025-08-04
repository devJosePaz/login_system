from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), ".env")
        extra = "ignore"

settings = Settings()

print("DEBUG: Current working directory =", os.getcwd())
print("DEBUG: .env file expected at =", os.path.abspath(".env"))
print("DEBUG: DATABASE_URL (from os.getenv) =", os.getenv("DATABASE_URL"))
