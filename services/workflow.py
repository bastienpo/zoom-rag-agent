import logging
import os

from llama_index.core import VectorStoreIndex
from llama_index.core.schema import NodeWithScore

from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Event,
    Workflow,
    step,
)
from llama_index.llms.together import TogetherLLM
from llama_index.vector_stores.qdrant import QdrantVectorStore

import qdrant_client

from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

_LOGGER = logging.getLogger(__name__)


class RetrieveEvent(Event):
    documents: list[NodeWithScore]


class RagAgentWorkflow(Workflow):
    llm = TogetherLLM(
        model="meta-llama/Meta-Llama-3-8B-Instruct-Lite",
        api_key=os.getenv("TOGETHER_API_KEY"),
    )

    _client = qdrant_client.QdrantClient(
        os.getenv("QDRANT_URL"),
        api_key=os.getenv("QDRANT_API_KEY"),
    )

    def __init__(self):
        self.vector_store = QdrantVectorStore(
            client=self._client,
            collection_name="user-data",
        )

    @step
    async def retrieve(self, event: StartEvent) -> RetrieveEvent:
        index = VectorStoreIndex.from_vector_store(self.vector_store)
        retriever = index.as_retriever()
        documents = await retriever.aretrieve(event.prompt)
        return RetrieveEvent(documents=documents)

    @step
    async def generation(self, event: RetrieveEvent) -> StopEvent:
        prompt = event.prompt
        content = await self.llm.acomplete(prompt)

        return StopEvent(result=str(content))


async def run_rag_agent_workflow() -> None:
    w = RagAgentWorkflow(timeout=60)
    print(await w.run(prompt="How are you?"))


if __name__ == "__main__":
    import asyncio

    asyncio.run(run_rag_agent_workflow())
