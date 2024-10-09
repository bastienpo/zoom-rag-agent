"""Configuration for the application."""

from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
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

    # Zoom configuration

    zoom_client_id: str = Field(
        description="The client ID for the Zoom API.",
    )

    zoom_client_secret: str = Field(
        description="The client secret for the Zoom API.",
    )

    zoom_verification_token: str = Field(
        description="The verification token for the Zoom API.",
    )

    # Qdrant configuration

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


settings = Settings()
