with open('output.txt','rb') as file:
    position = file.tell()
    print(f"Current Position: {position}")

    content = file.read(15)
    print(f"Read:  {content}")

    position = file.tell()
    print(f"Current Position: {position}")

    file.seek(2)
    print(f"Moved to position: {file.tell()}")

    content = file.read(4)
    print(f"Read from position 2: {content}")

    file.seek(2,1)
    content = file.read(3)
    print(f"Read after moving 2 from current: {content}")

    file.seek(4,2)
    content = file.read(3)
    print(f"Read after moving 3 from current: {content}")

    