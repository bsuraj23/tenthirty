class Demo:
    def __init__(self, value):
        self.value = value
    def __add__(self,other):
        return self.value + other.value

demo1= Demo(10)
demo2= Demo(20)
print(demo1 + demo2)  # Output: 30