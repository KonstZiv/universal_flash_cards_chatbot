from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Environment variables"""

    load_dotenv()
    class Config:
        case_sensitive = True


settings = Settings()