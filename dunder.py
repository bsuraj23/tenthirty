class Person:
    def _init_(self, name, age):
        # _init_ is called when the object is created
        self.name = name
        self.age = age

    def _str_(self):
        # _str_ controls what print() shows for the object
        return f"{self.name}, {self.age} years old"

    def _add_(self, other):
        # _add_ defines behavior for the + operator
        return self.age + other.age

# Creating two Person objects
p1 = Person("Arun", 30)
p2 = Person("Bob", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

print(p1 + p2)       # Output: 55 (adds ages using _add)