class Animal():
    def eat(self):
        print("Animal eat food")

class cat(Animal):
    def sound(self):
        print("cat meow")

class honey(cat):
    def weep(self):
        print("honey weeps")

a=Animal()
c=cat()
h=honey()
a.eat()
c.sound()
h.weep()