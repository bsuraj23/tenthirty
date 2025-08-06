#Constructor with 1 parameter
class Student:
    def __init__(self, name):
        self.name = name       

    def display(self):
        print("Student name is:", self.name)

# Create object and pass the name
s1 = Student("Sindhu")
s1.display()