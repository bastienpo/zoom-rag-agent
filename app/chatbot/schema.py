"""Schema for the chatbot."""

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class EventType(str, Enum):
    """The type of event."""

    ENDPOINT_URL_VALIDATION = "endpoint.url_validation"
    BOT_NOTIFICATION = "bot_notification"
    BOT_INSTALLED = "bot_installed"
    APP_DEAUTHORIZED = "app_deauthorized"


class Base(BaseModel):
    """Base model schema with pydantic config."""

    model_config = ConfigDict(
        arbitrary_types_allowed=False,
        extra="allow",
        validate_assignment=True,
    )


class Payload(Base):
    """The payload of a Zoom webhook."""

    account_id: str = Field(alias="accountId")
    channel_name: str = Field(alias="channelName")
    cmd: str = Field(alias="cmd")
    robot_jid: str = Field(alias="robotJid")
    timestamp: int = Field(alias="timestamp")
    to_jid: str = Field(alias="toJid")
    trigger_id: str = Field(alias="triggerId")
    user_id: str = Field(alias="userId")
    user_jid: str = Field(alias="userJid")
    user_name: str = Field(alias="userName")


class Notification(Base):
    """The notification from a Zoom webhook."""

    event: str = Field(description="The type of event.")
    payload: Payload = Field(description="The payload of the event.")
