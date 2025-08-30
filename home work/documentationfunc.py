#
def say_hello():
    print("hello,welcome to python!")

say_hello()
#function with parameter
def greet(name):
    print("hello", name)
greet("archana")
#fuction with return value
def add(a,b):
    return a+b
result=add(10,5)
print("sum is:", result)
#function with default fault parameter
def greet(name="guest"):
    print("hello", name)
greet("archu")
greet()
#5-fuction with multiple parameters
def multiply(x,y):
    return x*y
print(multiply(4,3))