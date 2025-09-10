Q:using the child object how we call parent name using same object in python?

In Python, when you have a child object (an instance of a subclass), you can access all the parent (superclass) attributes and methods directly using the child object. This is because the child class inherits everything from the parent class, unless overridden[3][5][9].
For example, if the parent class defines a name attribute, you can access it from the child object in this way:

PROGRAM:

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # calls the parent class constructor
        self.age = age

child_obj = Child("ParentName", 10)
print(child_obj.name)  # Accessing parent's 'name' attribute using child object


Here, child_obj.name refers to the name attribute that was defined in the parent[3][5].
- If you want to call a parent class method from the child object (even if overridden), you can use the super() function within the child class[6][9].
- If both parent and child define a method or attribute with the same name, the child’s version will override the parent’s by default. You can still access the parent’s version from within the child using super().