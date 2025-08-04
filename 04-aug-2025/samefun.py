class parent:
    def func(self):
        print("parent function")
    
class child(parent):
    def func(self):
        super().func()
        print("child")

c = child()
print(c.func)

