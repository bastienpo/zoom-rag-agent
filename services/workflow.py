import logging

from llama_index.llms.ollama import Ollama
from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
)

from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

_LOGGER = logging.getLogger(__name__)


class RagAgentWorkflow(Workflow):
    llm = Ollama(model="llama3.2:3b")

    @step
    async def generation(self, event: StartEvent) -> StopEvent:
        prompt = event.prompt
        content = await self.llm.acomplete(prompt)

        return StopEvent(result=str(content))


async def run_rag_agent_workflow() -> None:
    w = RagAgentWorkflow(timeout=10)
    print(await w.run(prompt="How are you?"))


if __name__ == "__main__":
    import asyncio

    asyncio.run(run_rag_agent_workflow())
