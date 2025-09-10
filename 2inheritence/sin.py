class Animal:
    def sound(self):
        print("Animal make sounds")
    
class cat(Animal):
    def sound(self):
        print("cat meow")

a=Animal()
c=cat()
a.sound()
c.sound()