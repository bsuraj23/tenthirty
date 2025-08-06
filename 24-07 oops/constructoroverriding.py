class parent:
    
    def add(self,a,b):
        print("i am an adding function")
    def __init__(self):
        print("parent constructor")
class child(parent):
    add=90+90

objp=parent()
objp.add(12,3)

objc=child()
