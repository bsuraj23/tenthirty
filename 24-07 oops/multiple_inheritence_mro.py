class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(B,C):
    pass

d=D()
d.show()
print(D.mro())   #output : B    here when you call D it check first and go to B first and C then A

