#class Animal:
  #  def speak(self):
 #       print("Animal speaks")

#class Dog(Animal):
  #  def speak(self):
 #       print("Dog barks")

# Polymorphism in action
#def make_animal_speak(animal):
 #   animal.speak()

#using super

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()      # Calls Animal's speak()
        print("Dog barks")   # Adds Dog's specific behavior