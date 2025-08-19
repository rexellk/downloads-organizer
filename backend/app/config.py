from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    app_name: str = "Downloads Organizer"
    cors_origins: List[str] = ["http://localhost:3000", "http://localhost:5173", "http://localhost:5174"]
    
    class Config:
        env_file = ".env"

settings = Settings()