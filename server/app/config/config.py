from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Optional
from typing import Literal


class Settings(BaseSettings):
    PROJECT_NAME: str = "FoodDetectorAPI"
    VERSION: str = "1.0.0"
    ENVIRONMENT: Literal["development", "staging", "production"] = "development"
    
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

    # # Database - теперь берутся из .env
    DATABASE_URL: str = "" #"mysql+aiomysql://root:root@localhost:3306/newschema"
    # # Или можно разбить на компоненты:
    # DB_HOST: str = "" #"localhost"
    # DB_PORT: int = 3306
    # DB_USER: str = "root"
    # DB_PASSWORD: str = "root"
    # DB_NAME: str = "newschema"
    
    @property
    def database_url(self) -> str:
        """Динамическое формирование DATABASE_URL из компонентов"""
        return f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Security
    SECRET_KEY: str = "your-secret-key-please-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: float = 9999999

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    # Модель конфигурации для Pydantic v2
    model_config = SettingsConfigDict(
        env_file=".env",           # Чтение из .env файла
        env_file_encoding="utf-8", # Кодировка файла
        case_sensitive=True,       # Чувствительность к регистру
        env_prefix="APP_",         # Префикс для переменных окружения (опционально)
        extra="ignore"             # Игнорировать лишние поля
    )


# Создаем экземпляр настроек
settings = Settings()