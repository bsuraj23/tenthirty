class student():
    def __init__(self, name , rollno):     # single inheritance 
        self.name= name
        self.rollno=rollno
        
    def info(self):
        print(f"Student name is {self.name} and and roll no is {self.rollno}")   
        
class engg(student):
    def __init__(self,name,rollno,branch):
        super().__init__(name,rollno)
        self.branch=branch
        
    def fullinfo(self):
        
        print(f" and his branch is {self.branch}")    
        
s1= engg("soham",1,"computer science")    
s1.info()
s1.fullinfo()    
                 
