#enumerator
word = "hello"

for i, char in enumerate(word):
    print(f"Index {i}: {char}")
    #enumerator-Return list with index
def get_with_index(items):
    return list(enumerate(items))

names = ['Archu', 'Bunny', 'Chinu']
print(get_with_index(names))

    # Add two numbers using lambda
add = lambda x, y: x + y
print(add(3, 5))

#1map() – Capitalize all names
names = ['khushi', 'saha', 'hithu']
capitalized = list(map(str.capitalize, names))
print(capitalized)
#map() – suares
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)
#map()-Cube of each number
numbers = [1, 2, 3, 4]
cubes = list(map(lambda x: x ** 3, numbers))
print("Cubes:", cubes)
 #map()-Convert list of strings to uppercase
names = ['archu', 'sindhu', 'swathi']
upper_names = list(map(lambda name: name.upper(), names))
print("Uppercase names:", upper_names)

#filter()-Get names with length > 3
names = ['Tom', 'Amy', 'Robert', 'Eve']
long_names = list(filter(lambda name: len(name) > 3, names))
print(long_names)
#Filter numbers greater than 10
numbers = [4, 11, 7, 15, 2, 30]
greater_than_10 = list(filter(lambda x: x > 10, numbers))
print("Numbers > 10:", greater_than_10)
#Filter words starting with 'a'
words = ['archana', 'rikky', 'ammu', 'cherry']
starts_with_a = list(filter(lambda word: word.startswith('a'), words))
print("Words starting with 'a':", starts_with_a)
#reduce() – Find the longest word
from functools import reduce

words = ['cat', 'elephant', 'tiger', 'lion']
longest = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print("Longest word:", longest)
 #reduce()-Multiply all numbers in a list
from functools import reduce

numbers = [2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)
#reduce()-Find max value in list using reduce
from functools import reduce

numbers = [10, 25, 8, 60, 32]
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum value:", maximum)
#reduce()-Find max value in tuple using reduce
from functools import reduce

numbers = (10, 25, 8, 50, 32)
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum value:", maximum)