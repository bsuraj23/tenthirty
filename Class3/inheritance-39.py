class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"
def area(self):
        return self.x * self.y
def perimeter(self):
        return 2 * self.x + 2 * self.y
def describe(self,text):
        self.description = text
def authorName(self,text):
        self.author = text
def scaleSize(self,scale):
        self.x = self.x * scale
    self.y = self.y * scale
#Code Example 7 - Using inheritance
class Square(Shape):
def __init__(self,x):
        self.x = x
	self.y = x
class DoubleSquare(Square):
def __init__(self,y):
        self.x = 2 * y
        self.y = y
def perimeter(self):
        return 2 * self.x + 3 * self.y
