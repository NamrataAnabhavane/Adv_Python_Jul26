from multiprocessing import Process
import time


def process_order(product):
    print(f"Processing order for {product.name}...")

    # Simulate processing time
    time.sleep(2)

    print(f"Order completed for {product.name}")


def process_orders(products):
    processes = []

    for product in products:
        process = Process(
            target=process_order,
            args=(product,)
        )

        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("\nAll orders have been processed successfully.")