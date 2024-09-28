"""Utility functions for the chatbot."""

from llama_index.core.vector_stores.types import VectorStore
from llama_index.vector_stores.qdrant import QdrantVectorStore

from app.config import QDRANT_API_KEY, QDRANT_COLLECTION, QDRANT_URL


def connect_to_vector_store() -> VectorStore:
    """Connect to the vector store.

    Support Qdrant local and cloud.

    Returns:
        VectorStore: The vector store.
    """
    return QdrantVectorStore(
        collection_name=QDRANT_COLLECTION,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
    )
