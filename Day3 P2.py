def say_hello(name):
    return f"Hello, {name}!"

# Assign the function to a variable (without parantheses)
greet_function = say_hello

print(greet_function("Namrata"))
print(say_hello("Namrata"))

# Passing the functions as arguments
def apply_operation(func,value):
    return func(value)

def double(x):
    return x * 2

#passing different function as an argument
print(apply_operation(double,5))

#Returning function from function
def make_multiplier(factor):
    def multiplier(x):
        return x*factor
    return multiplier

double = make_multiplier(20)
print(double(2))

# storing the function in data structure
operations = {
    'add': lambda x,y: x+y,
    'subtract': lambda x,y: x-y, 
}

print(operations['add'](10,5))
print(operations['subtract'](10,5))

