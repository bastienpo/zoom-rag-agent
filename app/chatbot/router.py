"""API for the chatbot."""

from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from app.chatbot.schema import EventType, Notification
from app.chatbot.utils import send_chat_message

router = APIRouter(tags=["Chatbot"], prefix="/v1")


@router.post("/webhook")
async def webhook_handler(notification: Notification) -> JSONResponse:
    """Handle webhook events from Zoom.

    Args:
        notification: The notification from the webhook.

    Returns:
        The response to the webhook event.

    """
    match notification.event:
        case EventType.BOT_NOTIFICATION:
            await send_chat_message(notification.payload.to_jid, "Hello, world!")

        case EventType.APP_DEAUTHORIZED | EventType.BOT_INSTALLED:
            pass

        case EventType.ENDPOINT_URL_VALIDATION:
            return JSONResponse(
                status_code=200,
                content={
                    "plainToken": notification.payload["plainToken"],
                },
            )

        case _:
            raise HTTPException(status_code=400, detail="Unsupported event type.")

    return JSONResponse(status_code=200, content={"status": "success"})
