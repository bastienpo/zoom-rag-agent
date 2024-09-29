"""API for the chatbot."""

from cadwyn import VersionedAPIRouter
from fastapi.responses import JSONResponse

from app.chatbot.schema import Message
from app.chatbot.service import generate_id

router = VersionedAPIRouter(tags=["Chatbot"], prefix="/v1")


@router.post(
    "/messages",
    response_model=Message,
    summary="Send messages to the chatbot.",
    dependencies=[],
)
async def send_messages(message: Message) -> JSONResponse:
    """Send messages to the chatbot."""
    return {
        "id": f"msg_{generate_id()}",
        "content": message.content,
    }
