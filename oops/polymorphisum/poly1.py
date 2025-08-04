class Circle():
    def area(self,r):
        self.r= r 
        return 3.14 * r * r
class Square():
    def area(self,s):
        self.s = s
        return s * s
shapes = [Circle(), Square()]

for shape in shapes:
    print(shape.area(5))  # Assuming a radius or side length of 5 for demonstration