# 1. What is an Actual Method ?
#The term "actual method" is not an official Python keyword — but it usually refers to a regular (instance) method of a class.

# Regular / Actual Method:


# Example:

class Person:
    def greet(self):  # This is a regular / actual method
        print("Hello!")

p = Person()
p.greet()  
# 2. What is a Class Method and How is It Rated (Used)?
 #Class Method:


# Example:

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school(cls):  # Class method
        return cls.school

print(Student.get_school())  