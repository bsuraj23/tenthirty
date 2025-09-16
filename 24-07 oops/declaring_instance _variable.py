class Student:
    def __init__(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age

obj=Student("john")
obj.set_age(22)
obj.age=20
print(obj.name)
print(obj.age)
