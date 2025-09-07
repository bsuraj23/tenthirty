class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def display(self):
        print("Child class method")

p = Child()   

p.show()    
p.display()