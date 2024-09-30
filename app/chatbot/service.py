"""Chatbot service."""

import logging
from uuid import uuid4

from llama_index.core import VectorStoreIndex
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.tools import FunctionTool
from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
)
from llama_index.llms.ollama import Ollama

from app.chatbot.utils import connect_to_vector_store

logger = logging.getLogger(__name__)


def generate_id() -> str:
    """Generate a random ID."""
    return f"msg_{uuid4().hex[:8]}"


def create_rag_tool() -> FunctionTool:
    """Create a RAG tool.

    Args:
        collection_name: The name of the collection to create the RAG tool for.

    Returns:
        FunctionTool: The RAG tool.
    """
    vector_store = connect_to_vector_store()
    index = VectorStoreIndex.from_vector_store(vector_store)

    query_engine = RetrieverQueryEngine(
        retriever=index.as_retriever(),
    )

    return FunctionTool.from_defaults(
        fn=query_engine.query,
        name="rag_tool",
        description=("Tool to answer user questions about the transcription data."),
    )


class MultiAgentWorkflow(Workflow):
    """Multi-agent workflow."""

    llm = Ollama(model="llama3.2:3b")

    @step
    async def generation(self, event: StartEvent) -> StopEvent:
        """Generation step."""
        prompt = event.prompt
        chat_message = ChatMessage(role=MessageRole.USER, content=prompt)

        rag_tool = create_rag_tool()

        response = await self.llm.achat_with_tools(
            tools=[rag_tool],
            user_msg=chat_message,
        )

        return StopEvent(result=str(response))
