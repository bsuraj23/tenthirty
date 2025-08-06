class parent:
    def __init__(self):
        self.parent_name = "I am parent!"
    def show_parent(self):
            print(self.parent_name)
class child(parent):
    def __init__(self):
         super().__init__() 
         self.child_name = "I am child!"
    def show_child(self):
              print(self.child_name)     
obj = child()
obj.show_parent()
# obj.show_child()     
