import os

from app.utils import load_from_env
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core.vector_stores.types import VectorStore


def connect_to_vector_store() -> VectorStore:
    """Connect to the vector store."""

    collection_name = load_from_env("QDRANT_COLLECTION")
    url = load_from_env("QDRANT_URL")
    api_key = os.getenv("QDRANT_API_KEY")

    store = QdrantVectorStore(
        collection_name=collection_name,
        url=url,
        api_key=api_key,
    )

    return store
