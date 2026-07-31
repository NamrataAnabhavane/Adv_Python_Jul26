import json

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
}
json_string = json.dumps(data)
print("JSON string:")
print(json_string)

parsed_data = json.loads(json_string)
print("Parsed data:")
print(parsed_data)

with open('data.json','w') as file:
    json.dump(data, file, indent = 2)

with open('data.json','r') as file:
    loaded_data = json.load(file)
    print("Loaded from file:")
    print(loaded_data)