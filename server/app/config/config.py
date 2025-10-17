from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "FoodDetectorAPI"
    VERSION: str = "1.0.0"
    API_STR: str = "/api"
    
    # Database
    DATABASE_URL: str = "mysql+mysqlconnector://root:root@localhost:3306/newschema"
    
    # Security
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    
    class Config:
        case_sensitive = True

settings = Settings()