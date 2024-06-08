import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(
            pathlib.Path(__file__).parent.parent.parent
        ) + "/.env",
        extra="ingore"
    )
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str


settings = SettingsConfigDict()
