import time
from threading import Thread

def cpu_bound_task():
    result = 0
    for i in range(10_000_000):
        result +=i
    return result

def io_bound_task():
    time.sleep(4)
    return "Done"

if __name__ == "__main__":
    print("Starting CPU based task")
    cpu_result = cpu_bound_task
    print("CPU bound result: ",cpu_result)

    print("Starting IO based task")
    io_result = io_bound_task()
    print("IO-bound result ",io_result)