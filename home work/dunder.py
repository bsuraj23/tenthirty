#1 __init__() – Constructor 
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Archana")
print(p.name)  
#2__str__() – String representation (used in print())
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"

p = Person("Archana")
print(p)  
# 3__len__() – Used by len() function
class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

obj = MyList([1, 2, 3])
print(len(obj))  
# 4__add__() – Operator overloading for 
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(10)
b = Number(5)
print(a + b)  
#5__getitem__() – Access elements like a list
class MyData:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

data = MyData([10, 20, 30])
print(data[1])  