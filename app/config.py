"""Configuration for the application."""

from decouple import Choices, config

ENVIRONMENT = config("ENVIRONMENT", default="dev", cast=Choices(["dev", "prod", "test", "staging"]))
QDRANT_URL = config("QDRANT_URL", default="http://localhost:6333")
QDRANT_API_KEY = config("QDRANT_API_KEY", default="")
QDRANT_COLLECTION = config("QDRANT_COLLECTION", default="default-collection")
