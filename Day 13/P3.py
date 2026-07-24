import asyncio
async def demo_task_states():

    task = asyncio.create_task(asyncio.sleep(2, result="Done"))

    print(f"Task pending: {not task.done()}")
    print(f"Task cancelled requested: {task.cancelled()}")

    await task

    print(f"Task pending: {task.done()}")
    print(f"Task result: {task.result()}")

    cancellable_task = asyncio.create_task(asyncio.sleep(5))

    await asyncio.sleep(1)
    print(f"Cancellable task")
    cancellable_task.cancel()

    try:
        await cancellable_task
    except asyncio.CancelledError:
        print("Task was cancelled")

    print(f"Task cancelled: {cancellable_task.cancelled()}")

asyncio.run(demo_task_states())