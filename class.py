# Define a class
class Student:
    # Constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display student info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Create an object of the class
s1 = Student("Saadwitha", 21)

# Call the method
s1.display_info()
