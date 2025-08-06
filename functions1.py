#enumerate
fruits = ["apple", "banana", "cherry", "date"]
for index, fruit in enumerate(fruits):
    print(f"Index {index} has fruit: {fruit}")

#lambda
add_10 = lambda x: x * 10
print(add_10(5))

#lambda with map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))
print(squared)

#lambda with filter
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

#lambda with reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", result)
