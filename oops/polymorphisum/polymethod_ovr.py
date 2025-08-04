class Parent:
    def greet(self):
        return "Hello from Parent"
class Child(Parent):
    def greet(self):
        return "Hello from Child"

obj= Child()
print(obj.greet())
print(Parent.greet(obj))  # This will call the Parent's greet method/
