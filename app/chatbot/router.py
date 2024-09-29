"""API for the chatbot."""

from cadwyn import VersionedAPIRouter

from app.chatbot.schema import MessageData, MessageResponse
from app.chatbot.service import MultiAgentWorkflow, generate_id

router = VersionedAPIRouter(tags=["Chatbot"], prefix="/v1")


@router.post(
    "/messages",
    response_model=MessageResponse,
    summary="Send messages to the chatbot.",
)
async def send_messages(data: MessageData) -> MessageResponse:
    """Send messages to the chatbot."""
    workflow = MultiAgentWorkflow()
    response = await workflow.run(prompt=data.content)

    return MessageResponse(
        id=f"msg_{generate_id()}",
        content=response,
    )
