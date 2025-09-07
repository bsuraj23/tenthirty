
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
from functools import reduce

# Sample list
numbers = [1, 2, 3, 4, 5, 6]

# 1. enumerate
print("Enumerate example:")
for index, value in enumerate(numbers):
    print(f"Index {index}: Value {value}")

# 2. lambda
square = lambda x: x * x
print("\nLambda example: square of 3 =", square(3))

# 3. map: Square each number
squares = list(map(lambda x: x ** 2, numbers))
print("Map + lambda (squares):", squares)

# 4. filter: Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Filter + lambda (evens):", evens)

# 5. reduce: Multiply all numbers together
product = reduce(lambda x, y: x * y, numbers)
print("Reduce + lambda (product):", product)

# 6. Generator function
def count_up_to_five():
    for i in range(1, 6):
        yield i

# Using the generator
gen = count_up_to_five()

print("Generator output:")
for number in gen:
    print(number)

