class Example:
    def add(self, *args):
        print("Sum is:", sum(args))

obj = Example()
obj.add(1, 2)          
obj.add(1, 2, 3, 4)   

#poly
class Example:
    def add(self, a, b, c=0):
        print("Sum is:", a + b + c)

obj = Example()
obj.add(2, 3)        
obj.add(2, 3, 4) 