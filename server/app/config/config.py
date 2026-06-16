from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Literal

class Settings(BaseSettings):
    PROJECT_NAME: str = "FoodDetectorAPI"
    VERSION: str = "1.0.0"
    ENVIRONMENT: Literal["development", "staging", "production"] = "development"
    
    API_STR: str = "/api"

    # Переменные для TiDB (будут загружены из окружения, имена как в Vercel)
    TIDB_HOST: str = ""
    TIDB_PORT: str = "4000"
    TIDB_USER: str = ""
    TIDB_PASSWORD: str = ""
    TIDB_DATABASE: str = ""

    @property
    def api_strings(self) -> dict:
        return {
            "General": f"{self.API_STR}/general",
            "User": {
                "Data": f"{self.API_STR}/user/data",
                "Statistic": f"{self.API_STR}/user/statistic"
            },
        }
    
    @property
    def rate_limiter_params(self) -> dict:
        return {"Times": 20, "Seconds": 60}

    @property
    def database_url(self) -> str:
        """Формирует URL для подключения к TiDB."""
        if self.TIDB_HOST and self.TIDB_USER and self.TIDB_PASSWORD and self.TIDB_DATABASE:
            return f"mysql+aiomysql://{self.TIDB_USER}:{self.TIDB_PASSWORD}@{self.TIDB_HOST}:{self.TIDB_PORT}/{self.TIDB_DATABASE}?ssl_ca=/etc/ssl/cert.pem"
        # fallback для локальной разработки (можно оставить старый URL)
        return "mysql+aiomysql://fastapi_user:userpassword123@localhost:3306/newschema"

    # Security
    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: float = 11

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        # Убираем префикс, чтобы переменные без APP_ загружались
        extra="ignore"
    )

settings = Settings()