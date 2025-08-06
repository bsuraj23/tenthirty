can a access the function of the child from the parent object in python?
You cannot directly access a child class's functions from a parent object in Python. ''Inheritance in Python is'
'designed so that a child class inherits properties and methods from the parent, but not the other way around.'
'If you create a parent class object and try to call a child class's method on it,you will get an AttributeError 
because the parent object does not know about the child’s methods.

For example:

class Parent:
    def show(self):
        print("In Parent")

class Child(Parent):
    def child_method(self):
        print("In Child")

obj = Parent()
obj.child_method()  # This will raise AttributeError

This will result in:
AttributeError: 'Parent' object has no attribute 'child_method'.

However, if you create an object of the child class, you can access both parent and child methods, due to inheritance.

In summary:
"Parent objects cannot access child methods, but child objects can access parent methods".