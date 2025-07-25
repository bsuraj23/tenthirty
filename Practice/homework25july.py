#To check whether the Parent object can access the child methods

class Parent:
    def start(self):
        print("Parent Class")
        
class Child(Parent):
    def child(self):
        print("Child Class")

v = Parent()
v.child()   

#Therefore, child -> parent is allowed
#But parent -> child is not allowed unless child method overrides or any advanced tricks are used



#Can super() be in the first line or can be in any line?

class Parent:
    def __init__(self):
        print("Parent constructor")

    def greet(self):
        print("Hello from Parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()  #FIRST in constructor
        print("Child constructor")

    def greet(self):
        print("Child says Hi")
        super().greet()      #Can be anywhere in the method
        print("Child ends greeting")

c = Child()
c.greet()

# so in __init__ constructor it should be in first line(ie as early as possible)
# and in the other methods it can be anywhere (ie before or after calling the parent method)
 