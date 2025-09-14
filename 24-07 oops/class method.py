class Student:
    school="Gitam"
    def __init__(self, name):
        self.name=name       #instance variable
    
    @classmethod
    def get_school(cls):    #here get get_school() is a class method
        return cls.school    #here cls.school is class variable
print(Student.get_school())   
