import pickle

data = {
        "firstName": "John",
        "lastName": "Doe",
        "age": 30,
        "isEmployed": True,
        "hobbies": ["reading", "traveling", "swimming"],
        "address": {
            "street": "123 Main Street",
            "city": "New York",
            "zipCode": "10001"
        },
    'scores': (85,99,24),
    'set_data': {1,2,3},
}

pickeled_bytes = pickle.dumps(data)
print("Pickled string:")
print(pickeled_bytes)

unpickeled_bytes = pickle.loads(pickeled_bytes)
print("Unpickled string:")
print(unpickeled_bytes)

print(f"Type preserved: {type(unpickeled_bytes['scores'])}")
print(f"Type preserved: {type(unpickeled_bytes['set_data'])}")

with open('data.pickle','wb') as file:
    pickle.dump(data, file)

with open('data.pickle','rb') as file:
    loaded_data = pickle.load(file)
    print("Loaded from pickle file:")
    print(loaded_data)