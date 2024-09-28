# import os

# import qdrant_client
# from llama_index.core import VectorStoreIndex
# from llama_index.core.query_engine import RetrieverQueryEngine
# from llama_index.core.tools import FunctionTool
# from llama_index.vector_stores.qdrant import QdrantVectorStore


# def create_qdrant_rag_tool(collection_name: str) -> FunctionTool:
#     """Create a RAG tool for a given collection name.

#     Args:
#         collection_name: The name of the collection to create the RAG tool for.
#     """

#     if not os.getenv("QDRANT_URL") or not os.getenv("QDRANT_API_KEY"):
#         raise ValueError("QDRANT_URL and QDRANT_API_KEY must be set.")

#     client = qdrant_client.QdrantClient(
#         os.getenv("QDRANT_URL"),
#         api_key=os.getenv("QDRANT_API_KEY"),
#     )

#     vector_store = QdrantVectorStore(
#         client=client,
#         collection_name=collection_name,
#     )

#     index = VectorStoreIndex.from_vector_store(vector_store)

#     query_engine = RetrieverQueryEngine(
#         retriever=index.as_retriever(),
#     )

#     return FunctionTool.from_defaults(
#         fn=query_engine.query,
#         name="RAG_tool",
#         description="Use this tool to answer user questions about the transcription data.",
#     )

import logging

from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
)

logger = logging.getLogger("uvicorn")


class RagAgentWorkflow(Workflow):
    llm = Ollama(model="llama3.2:3b")

    @step
    async def generation(self, event: StartEvent) -> StopEvent:
        prompt = event.prompt
        chat_message = ChatMessage(role=MessageRole.USER, content=prompt)
        content = await self.llm.achat([chat_message])

        return StopEvent(result=str(content))


# async def run_rag_agent_workflow() -> None:
#     w = RagAgentWorkflow(timeout=10)
#     print(await w.run(prompt="How are you?"))


# if __name__ == "__main__":
#     import asyncio

#     asyncio.run(run_rag_agent_workflow())
