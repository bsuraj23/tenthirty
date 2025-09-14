class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):       #Double underscore is called dunder which is starting and ending of the function name
        return f'Name:{self.name},Age:{self.age}'
    
s1=Student("Harish",21)
print(s1)