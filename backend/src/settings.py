from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict
from typing_extensions import Annotated


class Settings(BaseSettings):
    allowed_origins: Annotated[tuple[str, ...], NoDecode] = Field(default=())

    model_config = SettingsConfigDict(env_file=".env")

    @field_validator("allowed_origins", mode="before")
    @staticmethod
    def string_to_tuple(value: str | tuple[str, ...]) -> tuple[str, ...]:
        return tuple(value.split(",")) if isinstance(value, str) else value


@lru_cache
def get_settings() -> Settings:
    return Settings()
