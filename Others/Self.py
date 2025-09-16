
# About Self. 

# self is just a name we use inside a class in Python.

# *self is a reference to the current object (instance) of the class.

# *It is always the first parameter in instance methods.

# *It lets you access variables and methods of that particular object.

# *You don’t pass it when calling a method — Python passes it automatically.

# *Conventionally named self, but you could name it anything (not recommended).


# Real-life Example:

# Think of a blueprint of a house (class).
# When you build a real house from it (object),
# self means “this house”.

# code exemple:

class person:
    def __init__(self, name, age):
        self.name = "sunil"  
        self.age = age    

    def Greet(self):
        return "Hello its me Mr.sunil"

    def get_age(self):
        return f"{self.name} is {self.age} years old."
p1 = person("Mr.sunil", 21)
print(p1.Greet())
print(p1.get_age())


