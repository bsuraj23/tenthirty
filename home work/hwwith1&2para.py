#Constructor with 1 Parameter
class Student:
    def __init__(self, name): 
        self.name = name

    def display(self):
        print("Student Name:", self.name)

obj = Student("Archana")

obj.display()

#Constructor with 2 Parameters
class Student:
    def __init__(self, name, marks):  
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

obj = Student("Archana", 90)

obj.display()
