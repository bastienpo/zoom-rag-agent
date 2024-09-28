"""Configuration for the application."""

import os

from dotenv import find_dotenv, load_dotenv

ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")


def init_environment() -> None:
    """Initialize the environment."""
    if ENVIRONMENT == "dev":
        load_dotenv(find_dotenv())
