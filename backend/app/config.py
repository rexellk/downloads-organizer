"""Configuration settings for the Downloads Organizer application."""
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    app_name: str = "Downloads Organizer"
    cors_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173", 
        "http://localhost:5174"
    ]
    anthropic_api_key: str = ""

    class Config:
        """Pydantic configuration class."""
        env_file = ".env"


settings = Settings()