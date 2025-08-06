class Student:
    # Constructor to initialize object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display student details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create object of Student class
s1 = Student("Alice", 20)

# Access method using object
s1.display()
