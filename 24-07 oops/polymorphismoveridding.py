class parent:
    def greet(self):
        print("hello")
class child(parent):
    def greet(self):
        print("hey")

objp=parent()
objp.greet()
objc=child()
objc.greet()

