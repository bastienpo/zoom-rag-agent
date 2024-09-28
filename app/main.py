"""Main entry point for the application."""

from datetime import date

from cadwyn import Cadwyn, Version, VersionBundle
from cadwyn.structure.versions import HeadVersion

from app import chatbot

version_bundle = VersionBundle(
    HeadVersion(),
    Version(date(2024, 9, 27)),
)

app = Cadwyn(title="Zoom Rag Agent API", versions=version_bundle)
app.generate_and_include_versioned_routers(chatbot.router)
