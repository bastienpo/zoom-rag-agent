"""Main entry point for the application."""

from datetime import date

from cadwyn import Cadwyn, Version, VersionBundle
from cadwyn.structure.versions import HeadVersion

from app.config import init_environment

version_bundle = VersionBundle(
    HeadVersion(),
    Version(date(2024, 9, 27)),
)

app = Cadwyn(title="Zoom Rag Agent API", versions=version_bundle)

if __name__ == "__main__":
    init_environment()

# app.generate_and_include_versioned_routers(chatbot.router)
