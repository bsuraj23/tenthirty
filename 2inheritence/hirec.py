class parent():
    def names(self):
        print("parent child names")

class child1(parent):
    def name(self):
        print("child1 raju")

class child2(parent):
    def name(self):
        print("child2 pooja")

class child3(parent):
    def name(self):
        print("child3 swathi")

a=parent()
c1=child1()
c2=child2()
c3=child3()
a.names()
c1.name()
c2.name()
c3.name()
