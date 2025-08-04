class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person name is {self.name}")
    def add(self, a=0, b=0):
        res= a + b
        print(f"Sum is {res}")
        
obj= Person("John")
obj.add(5)
