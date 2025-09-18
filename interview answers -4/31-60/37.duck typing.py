#37.What is duck typing? Give an example.
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(entity):
    entity.quack()  # We just call quack(), no type checks

d = Duck()
p = Person()

make_it_quack(d)  # Quack!
make_it_quack(p)  # I'm quacking like a duck!
