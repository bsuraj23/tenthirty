class person:
    def __init__(self,name):
        self.name=name
        print(f"person: {self.name}")
    def add(self,a,b=15):
        result=a+b
        print(result)

pobj=person("Harish")
pobj.add(10)
#class student(person):
#    def __init__(self, name=suraj,)