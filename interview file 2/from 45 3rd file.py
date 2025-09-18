#45Write a script that imports a standard library (like `math`) and uses at least 3 functions.

import math

if __name__ == "__main__":
    number = 16

    print("Square root of", number, "is", math.sqrt(number))
    print("Factorial of", number, "is", math.factorial(number))
    print("Logarithm base 2 of", number, "is", math.log2(number))
    #NAMESPACES AND SCOPE
#46 Write a function that demonstrates the **LEGB rule** with nested functions.
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # local
    inner()
    print(x)      # enclosing
outer()
print(x)          # global
print(len("LEGB")) # built-in
#47. Implement a function that modifies a global variable using the `global` keyword.
# Global variable
count = 0
def increment():
    global count  # Tell Python we want to use the global variable
    count += 1
if __name__ == "__main__":
    print("Before:", count)  # 0
    increment()
    increment()
    print("After:", count)   # 2
#48 Implement a function that modifies an enclosed variable using the `nonlocal` keyword.
def outer():
    count = 0  # Enclosed variable
    def inner():
        nonlocal count  # Refers to the variable in the enclosing scope
        count += 1
        print("Inside inner():", count)
    inner()
    inner()
    print("Inside outer():", count)
if __name__ == "__main__":
    outer()
#49 Write a function with a variable that shadows a built-in function (e.g., `sum`) and fix it.
def calculate_sum(numbers):
    total = 0  # Use a different variable name
    for n in numbers:
        total += n
    return total
print(calculate_sum([1, 2, 3]))
#50 Demonstrate name collisions between global and local variables in a function
# Global variable
x = 10
def show_collision():
    x = 5  # Local variable shadows the global x
    print("Inside function:", x)
print("Global before function:", x)
show_collision()
print("Global after function:", x)
#51 Write code to read a text file and count the number of words.
file_path = "sample.txt"  # Replace with your file name
try:
    with open(file_path, "r") as file:
        text = file.read()
        words = text.split()      # Split by whitespace
        word_count = len(words)
    print(f"Number of words in '{file_path}': {word_count}")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
#52 Write a function that writes a list of numbers to a file (one per line)
def write_numbers_to_file(numbers, filename):
    with open(filename, "w") as file:
        for num in numbers:
            file.write(f"{num}\n")  # Write each number on a new line
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    write_numbers_to_file(nums, "numbers.txt")
    print("Numbers written to 'numbers.txt'")
#
#54Write code to serialize a dictionary into JSON and back
import json
# Original dictionary
data = {"name": "Archana", "age": 25, "city": "karimnagar"}
# Serialize to JSON string
json_str = json.dumps(data)
print("JSON string:", json_str)
# Deserialize back to dictionary
data_back = json.loads(json_str)
print("Dictionary:", data_back)
#Functional programming
# 56Use `map()` to square all elements of a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
#57Use `filter()` to extract only even numbers from a list.
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]
#58. Use `reduce()` to find the product of all numbers in a list.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
#59. Use a lambda function to sort a list of tuples by the second element.
tuples = [(1, 3), (2, 1), (4, 2)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Output: [(2, 1), (4, 2), (1, 3)]
#60. Combine `map`, `filter`, and `reduce` to compute the sum of squares of even numbers.
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
sum_squares_even = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
)
print(sum_squares_even)  # Output: 56 (2^2 + 4^2 + 6^2)


