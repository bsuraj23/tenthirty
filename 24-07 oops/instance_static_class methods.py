class Student:
    school="Gitam University"
    def __init__(self, name, age):
        self.name=name        #instance variable
        self.age=age          #instance variable
    
    #instance method
    def show_details(self):
        return f'name:{self.name},age:{self.age}'
    
    #static method
    @staticmethod
    def add(a,b):
        return a+b
    
    #class method
    @classmethod
    def get_school(cls):     #here get_school is a class method
        return cls.school    #here cls.school is a class variable
    
#How to use them
s1=Student("Harish",21)      #(instance)
print(s1.show_details())
#using static method
print(Student.add(5,5))
#using class method
print(Student.get_school())  

