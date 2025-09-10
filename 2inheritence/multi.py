class father():
    def role(self):
        print("father:father and son")

class mother():
    def role(self):
        print("mother:mother and daughter")

class child(father,mother):
    def role(self):
        father.role(self)
        mother.role(self)
        print("child:daughter or son")


c=child()
c.role()