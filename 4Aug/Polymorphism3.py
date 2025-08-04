
class Person:
    def __init__(self, name ="unknown",rollno=None):
        self.name= name
        self.rollno=rollno
        
    def display(self):
        print(f"Name :{self.name},Roll No :{self.rollno}")
        
s1 = Person()
s2= Person("Soham")
s3= Person("Amit",55)


s1.display()
s2.display()
s3.display()        