"""Schema for the chatbot."""

from pydantic import BaseModel, ConfigDict, Field


class Base(BaseModel):
    """Base model schema with pydantic config."""

    model_config = ConfigDict(
        arbitrary_types_allowed=False,
        extra="forbid",
        validate_assignment=True,
        strict=True,
    )


class MessageData(Base):
    """Message data schema."""

    content: str = Field(description="The content of the message.")
    stream: bool = Field(description="Whether the message is a stream.", default=False)


class MessageResponse(Base):
    """Message response schema."""

    id: str = Field(description="The ID of the message.")
    content: str = Field(description="The content of the message.")
