import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DATABASE_NAME = os.getenv("POSTGRES_DATABASE_NAME", "bot")
    POSTGRES_USER = os.getenv("POSTGRES_USER", "bot")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "bot")
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv("POSTGRES_PASSWORD")
    GOOGLE_API_KEY = os.getenv("POSTGRES_PASSWORD")

    class Config:
        case_sensitive = True


settings = Settings()
