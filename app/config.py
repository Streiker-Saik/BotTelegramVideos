from pathlib import Path
from typing import Optional

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.resolve()
env_patch = BASE_DIR / ".env"


class Settings(BaseSettings):
    """
    Класс для настройки подключения к базе данных Postgres.
    """

    POSTGRES_DB: str = "your_database_name_here"
    POSTGRES_USER: str = "your_user_name_here"
    POSTGRES_PASSWORD: str = "your_password_here"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    TELEGRAM_TOKEN: str = "your_telegram_token_here"

    HUGGING_TOKEN: str = "your_huggingface_token_here"

    DATABASE_URL: Optional[str] = None

    @model_validator(mode="before")
    def build_database_url(cls, values) -> dict:
        """Генерирует URL-адрес асинхронного подключения к базе данных Postgres."""

        values["DATABASE_URL"] = (
            f"postgresql+asyncpg://{values['POSTGRES_USER']}:{values['POSTGRES_PASSWORD']}@"
            f"{values['POSTGRES_HOST']}:{values['POSTGRES_PORT']}/{values['POSTGRES_DB']}"
        )
        return values

    model_config = SettingsConfigDict(env_file=env_patch, env_file_encoding="utf-8")


settings = Settings()
