import threading
import time

inventory.lock = threading.Lock()

def process_order(product,quantity):
    print(f"{threading.current_thread().name} started.")
    time.sleep(2)

    with inventory_lock:
        if product.quantity >= quantity:
            product.quantity -= quantity

            print(f"{product.name}: sold {quantity} items."
                f"Remaining: {product.quantity}"
            )
        else:
            print(f"{product.name}: Insufficient stock")
    print(f"{threading.current_thread().name} completed")

def process_orders(products):
    thread  = []
    order_quantities = [2,5,3]
    for product,qty in zip(products,order_quantities):
        thread = threading.Thread(
            target = process_order,
            args = (product,qty)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()