

class Character:
    def power(self):
        print("basic attack !")

class Hero(Character):
    def power(self):
        super().power()
        print("special power accessed")

h = Hero()
h.power()