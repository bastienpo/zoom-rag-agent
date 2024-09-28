"""API for the chatbot."""

from uuid import uuid4

from cadwyn import VersionedAPIRouter
from fastapi.responses import JSONResponse

from app.chatbot.schema import Message

router = VersionedAPIRouter(tags=["Chatbot"], prefix="/v1")


@router.post("/messages", tags=["Chatbot"])
async def send_messages(message: Message) -> JSONResponse:
    """Send messages to the chatbot."""
    return JSONResponse(
        status_code=200,
        content={
            "id": f"msg_{uuid4().hex[:8]}",
            "content": message.content,
        },
    )
