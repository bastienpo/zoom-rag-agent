"""API for the chatbot."""

import httpx
from cadwyn import VersionedAPIRouter
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = VersionedAPIRouter(tags=["Chatbot"], prefix="/v1")


class WebhookEvent(BaseModel):
    event: str
    payload: dict


@router.post("/webhook")
async def webhook(event: WebhookEvent) -> JSONResponse:
    """Handle webhook events from Zoom.

    Args:
        event: The webhook event.

    Returns:
        The response to the webhook event.

    """
    if event.event == "endpoint.url_validation":
        return JSONResponse(
            {
                "plainToken": event.payload["plainToken"],
                "encryptedToken": event.payload["encryptedToken"],
            }
        )

    if event.event == "app_mention":
        if event.payload["verification_token"] != ZOOM_CHATBOT_VERIFICATION_TOKEN:
            raise HTTPException(status_code=401, detail="Unauthorized")

        # Echo the message
        message = event.payload["message"]
        channel = event.payload["channel"]
        await send_chat_message(channel, f"You said: {message}")

    return JSONResponse({"status": "success"})
