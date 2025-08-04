class venkat:
    def speak(self):
        print("my child is narayana")

class narayana(venkat):
    def speak(self):
        print("my child is uday")

class uday(venkat):
    def speak(self):
        print("i am the last child")

b = venkat()
s1 = narayana()
s2 = uday()

b.speak()
s1.speak()
s2.speak()