"""Main entry point for the application."""

from collections.abc import Callable

from fastapi import FastAPI, Request, Response

from app import chatbot

app = FastAPI(title="Zoom Rag Agent API")


@app.middleware("http")
async def common_headers(request: Request, call_next: Callable) -> Response:
    """Add common headers to the response.

    Args:
        request: The incoming request.
        call_next: The next middleware or route handler to call.

    Returns:
        The response from the next handler.

    """
    response = await call_next(request)

    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; style-src 'self' fonts.googleapis.com; font-src fonts.gstatic.com"  # noqa: E501
    )
    response.headers["Referrer-Policy"] = "origin-when-cross-origin"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "deny"
    response.headers["X-XSS-Protection"] = "0"

    return response


app.include_router(chatbot.router)
