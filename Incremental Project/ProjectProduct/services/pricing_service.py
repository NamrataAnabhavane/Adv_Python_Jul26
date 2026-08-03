from functools import wraps

def audit(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Calculating price...")
        result = func(*args,**kwargs)

        print("\nCalculation completed")
        return result
    return wrapper

def discount(percent):
    def decorator(func):

        @wraps(func)
        def wrapper(product):
            discounted_price = product.price * (1 - percent/100)
            return func(product,discounted_price)
        return wrapper
    return decorator

def tax_calculator(rate):
    def calculate(price):

        return price * rate / 100
    return calculate

gst = tax_calculator(18)
@audit
@discount(10)
def calculate_price(product,discounted_price):
    tax = gst(discounted_price)

    final_price = discounted_price + tax

    return {
        "original": product.price,
        "discounted": discounted_price,
        "tax": tax,
        "final": final_price,
    }

def calculate_prices(products):
    return list(map(calculate_price,products))