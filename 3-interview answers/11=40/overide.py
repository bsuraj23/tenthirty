# Override the `__str__` method in a class to display custom output.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Override __str__ method
    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"


# Example usage
p1 = Person("sailu", 25)
p2 = Person("Balu", 30)

print(p1)  # Calls __str__()
print(p2)  # Calls __str__()
