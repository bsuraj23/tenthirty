#fun without parameters
def greet():
    print("Hello welcome to python!")

greet()


#fun with parameters
def add_numbers(a, b):
    result = a + b
    print("The sum is:", result)

add_numbers(5, 3)

#fun with return value
def multiply(x, y):
    return x * y
product = multiply(4, 6)
print("The product is:", product)


#fun with default parameters
def greet(name="Guest"):
    print("Hello,", name)
greet("alice")
greet()