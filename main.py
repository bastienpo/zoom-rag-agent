"""Main entry point for the application."""

from datetime import date
from cadwyn import Cadwyn, VersionBundle, Version

import os
from cadwyn.structure.versions import HeadVersion
from app.typing import Environment

ENVIRONMENT: Environment = os.getenv("ENVIRONMENT", "dev")

version_bundle = VersionBundle(
    HeadVersion(),
    Version(date(2024, 9, 27)),
)

app = Cadwyn(title="Zoom Rag Agent API", versions=version_bundle)

# app.generate_and_include_versioned_routers(chatbot.router)
