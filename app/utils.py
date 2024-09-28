"""Utility functions for the application."""

import os


def load_from_env(var_name: str) -> str:
    """Load a variable from the environment.

    Args:
        var_name (str): The name of the environment variable to load.

    Returns:
        str: The value of the environment variable.

    Raises:
        ValueError: If the environment variable is not set.
    """
    value = os.getenv(var_name)

    if value is None:
        raise ValueError(f"Missing environment variable: {var_name}")

    return value
