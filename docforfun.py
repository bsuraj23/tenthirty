#fun that prints msg
def say_hello():
    print("hello,welcome to python!")
say_hello()

#fun with parameters
def greet(name):
    print("hello!",name)
greet("saadwitha")

#fun with return value
def add(a,b):
    return a + b
result = add(10,15)
print("the sum is",result)

#fun with default parameter
def greet(name="guest"):
    print("Hello",name)
greet("saadwitha")
greet()

#fun with multiple parameter
def multiply(a,b):
    return a * b
result = multiply(2,2)
print("multiple is",result)