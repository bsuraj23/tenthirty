#Classmethod:
#Counting objects created
class Student:
    def __init__(self,name,age):
         self.name=name
         self.age=age
    @classmethod
    def from_string(cls,data):
         name,age=data.split('-')
         return cls(name,int(age))
s=Student.from_string("Sindhu-22")
print(s.name,s.age)

#Staticmethod:
class Math:
    @staticmethod
    def add(a,b):
        return a+b
print(Math.add(5,3))

