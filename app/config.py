"""Configuration for the application."""

from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AutoSettings(BaseSettings):
    """Settings for the application.

    Use this class to automatically load the settings from the environment variables.
    """

    model_config = SettingsConfigDict(
        arbitrary_types_allowed=True,
        validate_default=True,
        extra="ignore",
        strict=True,
        frozen=True,
        case_sensitive=False,
    )

    environment: Literal["dev", "prod", "test", "staging"] = Field(
        default="dev",
        description="The environment to run the application in.",
    )

    qdrant_url: str = Field(
        default="http://localhost:6333",
        description="The URL of the Qdrant vector database.",
    )

    qdrant_api_key: str = Field(
        default="",
        description="The API key to use for the Qdrant vector database.",
    )

    collection: str = Field(
        default="default-collection",
        description="The collection to use for the vector database.",
    )


settings = AutoSettings()
