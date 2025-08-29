class parent:
    def parent_function(self):
        print("This is parent class!")
class child(parent):
    def child_function(self):
        print("This is child class!")
c = child()
c.parent_function()