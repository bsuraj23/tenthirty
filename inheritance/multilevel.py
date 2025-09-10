#Simple multilevel inheritance
#Grandparent class
class Animal:
   def eat(self):
        print("The animal eats food")
#parent class
class Mammal(Animal):
    def walk(self):
        print("This mammal can walk")
#child class
class Dog(Mammal):
    def bark(self):
        print("Dog barks")
d=Dog()
d.eat()
d.walk()
d.bark()

#Using constructor(init)
class Grandparent:
    def __init__(self,gp_name):
        self.gp_name=gp_name
class parent(Grandparent):
    def __init__(self,gp_name,p_name):
        super().__init__(gp_name)
        self.p_name=p_name
class child(parent):
    def __init__(self,gp_name,p_name,c_name):
        super().__init__(gp_name,p_name)
        self.c_name=c_name
    def show_family(self):
        print("Grandparent",self.gp_name)
        print("parent",self.p_name)
        print("child",self.c_name)
c=child("Panduraj","Bhima","Ghatotkacha")
c.show_family()

#Using constructor2(init)
class university:
    def __init__(self,u_name):
        self.u_name=u_name
class college(university):
    def __init__(self,u_name,c_address):
        super().__init__(c_address)
        self.c_address=c_address
class student(college):
    def __init__(self,u_name,c_address,s_id):
        super().__init__(c_address,s_id)
        self.s_id=s_id
    def display(self):
        print("university",self.u_name)
        print("college",self.c_address)
        print("student",self.s_id)
s=student("JNTUH",503003,478)
s.display()