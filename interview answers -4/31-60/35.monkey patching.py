#35. What is monkey patching in Python?
class Dog:
    def speak(self):
        print("Woof!")

# Original behavior
d = Dog()
d.speak()  # Woof!

# Monkey patch the method
def new_speak(self):
    print("Bark Bark!")

Dog.speak = new_speak

d2 = Dog()
d2.speak()  # Bark Bark! (behavior changed at runtime)
