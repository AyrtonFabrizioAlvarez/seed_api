from functools import lru_cache
from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Backend Seed"
    app_version: str = "0.1.0"
    environment: str = "development"

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "backend_seed"
    postgres_user: str = "backend_seed"
    postgres_password: str = "backend_seed_dev"
    database_url: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def sqlalchemy_url(self) -> str:
        if self.database_url:
            return self.database_url

        user = quote_plus(self.postgres_user)
        password = quote_plus(self.postgres_password)
        database = quote_plus(self.postgres_db)
        return (
            f"postgresql+psycopg://{user}:{password}@{self.postgres_host}:"
            f"{self.postgres_port}/{database}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
