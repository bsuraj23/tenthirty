#Data Types & Variables
1#Write a function to check if a string is a palindrome without using slicing 
#using manual reverse string

def is_palindrome(s):
    reverse = ""
    for char in s:
        reverse = char + reverse
    return s == reverse
print(is_palindrome("madam"))  
print(is_palindrome("world"))  
#2Given a list of numbers, remove all duplicates **without using set()**.
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))  # [1, 2, 3, 4, 5]
#3Implement a function to merge two dictionaries.
def merge_dicts(d1, d2):
    result = d1.copy()  # start with first dictionary
    for key, value in d2.items():  # add items from second dictionary
        result[key] = value
    return result
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

print(merge_dicts(dict1, dict2))  # {'a': 1, 'b': 3, 'c': 4}
#4Write code to find the frequency of each character in a string. simple give more programs
def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
text = "hello"
print(char_frequency(text))  # {'h':1, 'e':1, 'l':2, 'o':1}
#5Implement your own version of max() without using the built-in function.
def my_max(lst):
    if not lst:
        return None
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum
numbers = [10, 4, 7, 22, 15]
print(my_max(numbers))  # 22
#Lists, Strings & Collections
#6Reverse a list **in place** without using [::-1] or reverse().
s="hello"
rev="".join(reversed(s))
print(rev)
#7Write code to flatten a nested list (e.g. [[1,2],[3,4]] → [1,2,3,4]).
nested=[[1,2],[3,4]]
flat=[x for sub in nested for x in sub]
print(flat)
#8Given a string, count the number of vowels and consonants.
string=input("enter a string:").lower()
vowels='aeiou'
print("vowels in the string")
for char in string:
     if char in vowels:
         print(char,end='')
#9Find the second largest number in a list
def second_largest(lst):
    lst = list(set(lst))  # Remove duplicates
    lst.sort()            # Sort the list
    return lst[-2]        # Return second largest
numbers = [10, 20, 4, 45, 99]
print(second_largest(numbers)) 
#10Rotate a list by k elements (circular shift).
def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # Handle k larger than list length
    lst[:] = lst[-k:] + lst[:-k]  # Circular shift

# Example
numbers = [1, 2, 3, 4, 5]
rotate_list(numbers, 2)
print(numbers)  # Output: [4, 5, 1, 2, 3]
#Control Flow & Loops

#11. Print the Fibonacci sequence up to `n` terms.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
n = 10
fibonacci(n)  # Output: 0 1 1 2 3 5 8 13 21 34

#12. Write a program to print a multiplication table for a number.
num = int(input("Enter a number: "))
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(num * i, end=' ')

#13. Write code to find all prime numbers up to `n`.
n = int(input("Enter a number: "))
primes = []
for num in range(2, n+1):
    if all(num % i != 0 for i in range(2, num)):
        primes.append(num)
print(primes)

#14. Implement a function to check if two strings are anagrams.
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False

#15. Find all numbers between 1 and 100 divisible by both 3 and 5.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
#Functions
#16. Write a function that takes \*args and \*\*kwargs and prints them separately.
def show_args_kwargs(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
show_args_kwargs(1, 2, 3, name="Alice", age=25)

#17. Implement a recursive function to calculate factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of 1:", factorial(1))
print("Factorial of 6:", factorial(6))
print("Factorial of 3:", factorial(3))
print("Factorial of 7:", factorial(7))
print("Factorial of 8:", factorial(8))
print("Factorial of 10:", factorial(10))
#18. Implement a recursive function to compute Fibonacci numbers.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("Fibonacci of 0:", fibonacci(0))  # 0
print("Fibonacci of 1:", fibonacci(1))  # 1
print("Fibonacci of 5:", fibonacci(5))  # 5
print("Fibonacci of 6:", fibonacci(6))  # 8
print("Fibonacci of 7:", fibonacci(7))  # 13
print("Fibonacci of 10:", fibonacci(10)) # 55

#19. Write a function that accepts a list and returns a new list with only unique elements.
def unique_elements(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))
print(unique_elements(['a', 'b', 'a', 'c', 'b']))
print(unique_elements([5, 5, 5, 5]))
print(unique_elements([]))
print(unique_elements([1, 2, 3, 4, 5]))

#20. Write a function that returns the sum of digits of a number.
def sum_of_digits(n):
    return sum(map(int, str(abs(n))))
print(sum_of_digits(123))    # 6
print(sum_of_digits(4567))   # 22
print(sum_of_digits(0))      # 0
print(sum_of_digits(-89))    # 17
print(sum_of_digits(1001))   # 2
 #OOP in Python
#21. Create a class `BankAccount` with methods `deposit`, `withdraw`, and `check_balance`.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
    def check_balance(self):
        return self.balance
acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.check_balance())  # 120

#22. Implement inheritance with a base class `Shape` and derived classes `Circle` and `Rectangle` with an `area()` method.
class Shape:
    def info(self):
        print("This is Shape")
class Rectangle(Shape):
    def area(self):
        print("Area = l * b")
class Circle(Shape):
    def area(self):
        print("Area = pi * r * r")
c = Circle()
c.info()
c.area()
r = Rectangle()
r.info()
r.area()

#23. Implement a class with a **static method** to check if a number is even.
class NumberUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0
print(NumberUtils.is_even(4))   # True
print(NumberUtils.is_even(7))   # False
print(NumberUtils.is_even(0))   # True
print(NumberUtils.is_even(-2))  # True

#24. Create a class `Car` that tracks the number of cars created using a **class variable**.
class Car:
    count = 0  # Class variable shared across all instances
    def __init__(self, model):
        self.model = model
        Car.count += 1  # Increment the shared class variable
car1 = Car("Sedan")
car2 = Car("SUV")
print("Total cars created:", Car.count)  # 2

#25. Override the `__str__` method in a class to display custom output.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
p = Person("Alice", 30)
print(p)  # Person(name=Alice, age=30)
#Iterators & Generators
#26. Create a custom iterator class that generates square numbers up to `n`.
class SquareIterator:
    def __init__(self, n):
        self.i, self.n = 1, n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        val = self.i ** 2
        self.i += 1
        return val

# Example usage
for sq in SquareIterator(5):
    print(sq)

#27. Write a generator function that yields even numbers up to `n`.
def even_numbers(n):
    for i in range(2, n+1, 2):
        yield i
for num in even_numbers(10):
    print(num)

#28. Implement a generator that yields Fibonacci numbers.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)

#29. Write a generator that reads a large file line by line.
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.rstrip('\n')  # remove trailing newline
for line in read_large_file('large_file.txt'):
    print(line)

#30. Create a generator that yields prime numbers up to `n`.
def primes(n):
    for num in range(2, n+1):
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            yield num
# Example usage:
for p in primes(20):
    print(p)


