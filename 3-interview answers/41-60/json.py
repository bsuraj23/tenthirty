import json

data = {"name": "Alice", "age": 25, "city": "New York"}

# Serialize to JSON string
json_str = json.dumps(data)
print("Serialized JSON:", json_str)

# Deserialize back to Python dictionary
data_back = json.loads(json_str)
print("Deserialized dictionary:", data_back)
