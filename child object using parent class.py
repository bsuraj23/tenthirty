class Animal:
    def sound(self):
        print("Animal makes a sound")

class dog(Animal):
    def sound(self):
        print("dog barks")

class cat(Animal):
    def sound(self):
        super().sound()  
        print("meow")

d1 = dog()
c1 = cat()

c1.sound() 
d1.sound()
