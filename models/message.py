from pydantic import BaseModel


class Message(BaseModel):
    content: str
    stream: bool = False
