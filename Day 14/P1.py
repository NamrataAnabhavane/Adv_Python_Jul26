import asyncio

async def slow_operation():
    print("Starting operation starting")
    await asyncio.sleep(2)  
    return "Slow result"

async def demo_await_vs_task():
    print("Using await")
    result = await slow_operation()
    print(f"Result: {result}")

    print("Create Task")
    task = asyncio.create_task(slow_operation())

    print("Task is running is background")

    await asyncio.sleep(1)

    print("This prints here")

    result = await task
    print(f"Result: {result}")
asyncio.run(demo_await_vs_task())  
