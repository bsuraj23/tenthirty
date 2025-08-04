class Parent:
    def greet(self ):
        print("parent ")
        
class Child(Parent):
    def greet(self ):
        super().greet()   #  child accessing parent method
        print("child ")
        
c= Child()
c.greet()   
        
class rect:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth        #creating list of obj
        
    def area(self ):
        return self.length*self.breadth
        
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self ):   
        return 3.14*self.radius*self.radius
    
shapes = [rect(3,4),circle(5)]
for shape in shapes:
    print(shape.area())      