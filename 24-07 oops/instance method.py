class Student:
    def __init__(self, name, marks):
        self.name=name   #instance variable
        self.marks=marks  #instance variable
    
    #instance method
    def display_info(self):
        print(f'Name:{self.name},marks:{self.marks}')
s1=Student("Harish",100)
s2=Student("Anu",95)

#calling instance methods
s1.display_info()
s2.display_info()

