#Parent class
class Animal:
    def sound(self):
        return "Animal makes a sound"

# Child class overriding the parent class method
class Dog():
    def sound(self):
        return "Dog Barks!"

class Cat():
    def sound(self):
        return "Meow!" 

# Function to demonstrate polymorphism
Ani =[Animal(),Dog(), Cat()]
for i in Ani:
    print(i.sound())  # Calls the overridden method in each subclass
     