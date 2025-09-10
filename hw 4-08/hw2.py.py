#Access the functions of the child object from the parent object
class Parent:
    def call_child_function(self):
        print("Inside Parent method")
        self.child_function()  # This will call child's version if overridden

    def child_function(self):
        print("Parent's version of child_function (can be overridden)")

class Child(Parent):
    def child_function(self):
        print("Child's version of child_function")

# Create a child object
obj = Child()

# Call parent method
obj.call_child_function()