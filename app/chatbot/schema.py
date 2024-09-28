from pydantic import BaseModel, Field


class Message(BaseModel):
    content: str
    stream: bool = Field(default=False)
