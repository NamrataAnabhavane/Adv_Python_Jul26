import asyncio
import time

async def task1():
    print("Starting Asychronous work")

    print("Task 1.1: Starting")
    await asyncio.sleep(2)
    print("Task 1.1 done")

    print("Task 1.2: Starting")
    await asyncio.sleep(2)
    print("Task 1.2 done")

    print("All Asynchronous work done")

async def task2():
    print("Starting Asychronous work")

    print("Task 2.1: Starting")
    await asyncio.sleep(2)
    print("Task 2.1 done")

    print("Taskk 2.2: Starting")
    await asyncio.sleep(2)
    print("Task 2.2 done")

    print("All Asynchronous work done")

async def task3():
    print("Starting Asychronous work")

    print("Task 3.1: Starting")
    await asyncio.sleep(2)
    print("Task 3.1 done")

    print("Taskk 3.1: Starting")
    await asyncio.sleep(2)
    print("Task 3.2 done")

    print("All Asynchronous work done")

async def run_concurrently():
    print("Start concurrent execution")

    start = time.time()

    results = await asyncio.gather(
        task1(),
        task2(),
        task3()
    )
    print(f"All tasks completed in {time.time() - start:.2f}s")
    print(f"Results: {results}")

asyncio.run(run_concurrently())