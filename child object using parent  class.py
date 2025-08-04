class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Polymorphism in action
def make_animal_speak(animal):
    animal.speak()