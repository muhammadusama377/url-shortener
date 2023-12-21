from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./.env", env_file_encoding="utf-8", extra="ignore"
    )

    database_dsn: PostgresDsn
    postgres_server: str
    postgres_user: str
    postgres_db: str
    postgres_password: str
    host: str


settings = Settings()
