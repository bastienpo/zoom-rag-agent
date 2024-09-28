"""Utility functions for the chatbot."""

import os

from llama_index.core.vector_stores.types import VectorStore
from llama_index.vector_stores.qdrant import QdrantVectorStore

from app.utils import load_from_env


def connect_to_vector_store() -> VectorStore:
    """Connect to the vector store.

    Returns:
        VectorStore: The vector store.
    """
    collection_name = load_from_env("QDRANT_COLLECTION")
    url = load_from_env("QDRANT_URL")
    api_key = os.getenv("QDRANT_API_KEY")

    return QdrantVectorStore(
        collection_name=collection_name,
        url=url,
        api_key=api_key,
    )
