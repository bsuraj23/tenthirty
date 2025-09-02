# Create a dictionary with dictionary values
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grade": "A"
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "grade": "B"
    },
    "student3": {
        "name": "Charlie",
        "age": 21,
        "grade": "A"
    }
}

# Accessing a nested value
print("Student3 Name:", students["student3"]["name"])

# Updating a nested value
students["student1"]["grade"] = "B+"

# Adding a new nested dictionary
students["student4"] = {
    "name": "David",
    "age": 23,
    "grade": "A"
}

# Loop through all students and print details
print("\nAll Student Details:")
for student_id, info in students.items():
    print(f"{student_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()  # blank line for readability
