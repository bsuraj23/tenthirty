class human:
    def speak(self):
        print("talk")

class sai(human):
    def speak(self):
        print("hiii")

class sashi(human):
    def speak(self):
        print("hello")
        
h1=human
s1=sai
s2=sashi

s1.speak(human)
s2.speak(human)