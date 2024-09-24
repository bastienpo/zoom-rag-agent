from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
)


class MyWorkflow(Workflow):
    @step
    async def my_step(self, event: StartEvent) -> StopEvent:
        import time

        time.sleep(1)
        return StopEvent(result="done")


async def main():
    w = MyWorkflow(timeout=10, verbose=True)
    print(await w.run())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
