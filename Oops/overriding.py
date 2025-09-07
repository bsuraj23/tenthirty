class Person:
    def __init__(self, name):
        self.name=name
        print(f"person: {self.name}")
    def add(self,a,b=20):
        result=a+b
        print(result)
pobj=Person("Rizwan")
pobj.add(20)













