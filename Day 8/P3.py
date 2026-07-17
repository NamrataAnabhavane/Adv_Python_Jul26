file = None
try:
    file = open('example.txt', 'r')
    content = file.read()
    print(content)
finally:
    if file:
        file.close()

with open('input.txt','r') as input_file, open('output.txt','w') as output_file:
    content = input_file.read()
    output_file.write(content.upper())