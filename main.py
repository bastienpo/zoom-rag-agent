from datetime import date
from cadwyn import Cadwyn, VersionBundle, Version

from cadwyn.structure.versions import HeadVersion
from api import chatbot

version_bundle = VersionBundle(
    HeadVersion(),
    Version(date(2024, 9, 24)),
)

app = Cadwyn(title="Zoom Rag Agent API", versions=version_bundle)

app.generate_and_include_versioned_routers(chatbot.router)
