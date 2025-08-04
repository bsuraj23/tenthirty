class Babu:
    def speak(self):
        print("my child is satyanarayana")

class Satyanarayana(Babu):
    def speak(self):
        print("my child is Sai")

class Sai(Babu):
    def speak(self):
        print("i am the last child")

b = Babu()
s1 = Satyanarayana()
s2 = Sai()

b.speak()
s1.speak()
s2.speak()
