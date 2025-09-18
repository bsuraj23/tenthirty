class Parent:
    def display(self):
        print("This is the Parent class")

# Child class that overrides display
class Child(Parent):
    def display(self):
        super().display()  # Call Parent's display method
        print("This is the Child class")

# Creating objects
pobj = Parent()
pobj.display()

print("---------------")

cobj = Child()
cobj.display()

# can parent object access child object
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def child_method(self):
        print("Child-specific method")

# Creating parent object
p = Parent()
p.show()
