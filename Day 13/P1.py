import time
import asyncio
def sync_work():
    print("Starting Sychronous work")

    print("Taskk 1: Starting")
    time.sleep(2)
    print("Task 1 done")

    print("Taskk 2: Starting")
    time.sleep(2)
    print("Task 2 done")

    print("All Synchronous work done")

#sync_work()

async def async_work():
    print("Starting Asychronous work")

    print("Task 1: Starting")
    await asyncio.sleep(2)
    print("Task 1 done")

    print("Task 2: Starting")
    await asyncio.sleep(2)
    print("Task 2 done")

    print("All Asynchronous work done")

start = time.time()
sync_work()
print(f"Synchronous: {time.time() - start:.2f}s")

start1 = time.time()
asyncio.run(async_work())
print(f"Asynchronous: {time.time() - start1:.2f}s")
