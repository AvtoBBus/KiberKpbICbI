from pydantic_settings import BaseSettings
from typing import List
from typing import Literal


class Settings(BaseSettings):
    PROJECT_NAME: str = "FoodDetectorAPI"
    VERSION: str = "1.0.0"

    API_STR: str = "/api"

    @property
    def api_strings(self) -> object:
        return {
            "General": f"{self.API_STR}/general",
            "User": {
                "Data": f"{self.API_STR}/user/data",
                "Statistic": f"{self.API_STR}/user/statistic"
            },
        }



    # Database
    DATABASE_URL: str = "mysql+aiomysql://root:root@localhost:3306/newschema"

    # Security
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: float = 9999999

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    class Config:
        case_sensitive = True


settings = Settings()
