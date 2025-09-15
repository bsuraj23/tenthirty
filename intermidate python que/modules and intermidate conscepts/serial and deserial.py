import json

# A Python dictionary
person = {
    "name": "Swathi",
    "age": 21,
    "is_student": False
}

# --- Serialization ---
# Convert Python object to JSON string
json_string = json.dumps(person)
print("Serialized (Python -> JSON):")
print(json_string)

# --- Deserialization ---
# Convert JSON string back to Python object
python_obj = json.loads(json_string)
print("\nDeserialized (JSON -> Python):")
print(python_obj)
