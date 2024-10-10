"""Utility functions for the chatbot."""

from enum import Enum

import httpx
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


async def get_access_token() -> str:
    """Get the access token for the Zoom API.

    Returns:
        The access token for the Zoom API.

    """
    data = {
        "grant_type": "client_credentials",
        "client_id": settings.zoom_client_id,
        "client_secret": settings.zoom_client_secret,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(settings.zoom_oauth_url, data=data)
        return response.json()["access_token"]


async def send_chat_message(channel: str, message: str) -> dict:
    """Send a chat message to a Zoom channel.

    Args:
        channel: The Zoom channel to send the message to.
        message: The message to send.

    Returns:
        The response from the Zoom API.

    """
    headers = {
        "Authorization": f"Bearer {await get_access_token()}",
        "Content-Type": "application/json",
    }

    data = {
        "robot_jid": settings.zoom_bot_jid,
        "to_jid": channel,
        "user_jid": channel,
        "content": {
            "head": {"text": "Zoomby"},
            "body": [{"type": "message", "text": message}],
        },
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            settings.zoom_message_url, headers=headers, json=data
        )
        return response.json()
