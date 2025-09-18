# Class Method (@classmethod)
#  Why we use:

# *Because sometimes you want a method that works with the class itself, not just with individual objects.
# *It can access or modify class variables that are shared among all instances.
# *Often used as factory methods (alternative constructors).

# When to use:

# *When you need to do something at the class level (not tied to one specific object).
# *Example: Creating objects in different ways, or keeping track of total objects created.

# Example:

class Student:
    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1

    @classmethod
    def get_total_students(cls):
        return cls.total_students

s1 = Student("MR.Sunil💕")
s2 = Student("Miss.SONA💕")

print(Student.get_total_students())  
# Output: 2

# Static Method (@staticmethod)
# Why we use:

# *Because sometimes you need a method inside a class that doesn’t depend on class or instance.
# *It’s like a normal function but kept inside the class for better organization.

# When to use:

# When the method is logically related to the class, but it doesn’t need self or cls.
# *Example: Utility/helper functions (like validation, formatting, calculations).


# Example: of Static Method
class Person:
    def __init__(self, name, age):
        if Person.is_valid_age(age):   # using static method
            self.name = name
            self.age = age
        else:
            raise ValueError("Invalid age")

    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 100


#  Valid case
p1 = Person("Mr.Sunil💕", 21)
print(p1.name, p1.age)    

#  Invalid case
p2 = Person("Miss Sona💕", 18)
print(p2.name, p2.age)




