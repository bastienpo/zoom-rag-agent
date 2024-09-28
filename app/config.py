from dotenv import load_dotenv, find_dotenv
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")


def init_environment() -> None:
    """Initialize the environment."""
    if ENVIRONMENT == "dev":
        load_dotenv(find_dotenv())
