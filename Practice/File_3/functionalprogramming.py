#Functional Programming

#Use map() to square all elements of a list
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

#Use filter() to extract only even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

#Use reduce() to find the product of all numbers in a list
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)

#Use a lambda function to sort a list of tuples by the second element
pairs = [(1, 5), (2, 1), (3, 4), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted by second element:", sorted_pairs)

#Combine map, filter, and reduce to compute the sum of squares of even numbers
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
result = reduce(lambda x, y: x + y,
                map(lambda x: x**2,
                    filter(lambda x: x % 2 == 0, numbers)))
print("Sum of squares of even numbers:", result)