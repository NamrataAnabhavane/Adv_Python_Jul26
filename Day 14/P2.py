with open('sample.txt','w') as file:
    file.write("Hello")
with open('sample.txt','r') as file:
    content = file.read()
    print("Entire file:")
    print(content)

with open('sample.txt','r') as file:
    chunk = file.read(10)
    print(f"First 10 chars: {chunk}")

with open('sample.txt','r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"Line 1: {line1.strip()}")
    print(f"Line 2: {line1.strip()}")

with open('sample.txt','r') as file:
    lines = file.readlines()
    print(lines)

with open('sample.txt','r') as file:
    for line in file:
        print(line.strip())