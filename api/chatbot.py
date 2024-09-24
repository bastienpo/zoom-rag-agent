from cadwyn import VersionedAPIRouter
from models import Message
from fastapi.responses import ORJSONResponse, HTTPException

from uuid import uuid4

router = VersionedAPIRouter(tags=["Chatbot"], prefix="/v1")


@router.post("/messages", response_class=ORJSONResponse)
async def messages(message: Message):
    if message.stream:
        return HTTPException(status_code=501, detail="Streaming is not implemented")

    return ORJSONResponse(
        status_code=200,
        content={
            "id": f"msg_{uuid4().hex[:8]}",
            "content": message.content,
        },
    )
