"""Main entry point for the application."""

from datetime import date

from cadwyn import Cadwyn, Version, VersionBundle

from app import chatbot

version_bundle = VersionBundle(
    Version(date(2024, 10, 9)),
)

app = Cadwyn(title="Zoom Rag Agent API", versions=version_bundle)
app.generate_and_include_versioned_routers(chatbot.router)
