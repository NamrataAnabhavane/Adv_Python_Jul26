def simple_generator():
    print("Step1: 1st yield")
    yield 1

    print("Step2: 2nd yiels")
    yield 2

    print("Step2: 23rd yiels")
    yield 3

    print("Generator is done")

gen = simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))