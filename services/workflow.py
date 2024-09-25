import logging
import os

from llama_index.utils.workflow import draw_all_possible_flows

from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Event,
    Workflow,
    step,
)
from llama_index.llms.together import TogetherLLM
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

_LOGGER = logging.getLogger(__name__)


class GenerationEvent(Event):
    content: str


class RagAgentWorkflow(Workflow):
    llm = TogetherLLM(
        model="meta-llama/Meta-Llama-3-8B-Instruct-Lite",
        api_key=os.getenv("TOGETHER_API_KEY"),
    )

    @step
    async def generation(self, event: StartEvent) -> GenerationEvent:
        if not event.prompt:
            raise ValueError("Prompt is required.")

        prompt = event.prompt
        content = await self.llm.acomplete(prompt)

        return GenerationEvent(content=str(content))

    @step
    async def identity(self, event: GenerationEvent) -> StopEvent:
        return StopEvent(result=event.content)


async def run_rag_agent_workflow():
    w = RagAgentWorkflow(timeout=60)
    print(await w.run(prompt="How are you?"))


if __name__ == "__main__":
    import asyncio

    asyncio.run(run_rag_agent_workflow())
