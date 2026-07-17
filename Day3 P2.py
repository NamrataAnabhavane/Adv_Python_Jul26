def say_hello(name):
    return f"Hello, {name}!"

greet_function = say_hello

print(greet_function("Namrata"))
print(say_hello("Namrata"))

def apply_operation(func,value):
    return func(value)

def double(x):
    return x*2

print(apply_operation(double,5))

def make_multiplier(factor):
    def mulitiplier(x):
        return x*factor
    return mulitiplier

double = make_multiplier(20)
print(double(2))

operations = {
    'add': lambda x,y: x+y,
    'sub': lambda x,y: x-y,
}
print(operations['add'](10,5))
print(operations['sub'](10,5))