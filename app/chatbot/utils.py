"""Utility functions for the chatbot."""

from llama_index.core.vector_stores.types import VectorStore
from llama_index.vector_stores.qdrant import QdrantVectorStore

from app.config import settings


def connect_to_vector_store() -> VectorStore:
    """Connect to the vector store.

    Support Qdrant local and cloud.

    Returns:
        VectorStore: The vector store.
    """
    return QdrantVectorStore(
        collection_name=settings.collection,
        url=settings.qdrant_url,
        api_key=settings.qdrant_api_key,
    )
