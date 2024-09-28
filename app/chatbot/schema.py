"""Schema for the chatbot."""

from pydantic import BaseModel, Field


class Message(BaseModel):
    """Message schema."""

    content: str = Field(description="The content of the message.")
    stream: bool = Field(description="Whether the message is a stream.", default=False)
