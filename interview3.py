#Data Types & Variables
#Check if a string is a palindrome (without slicing)
def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome("madam"))    
print(is_palindrome("python"))   
print(is_palindrome("table")) 


#Remove duplicates from a list (without set())
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
nums = [1, 2, 2, 3, 4, 3, 5, 1, 6]
print(remove_duplicates(nums)) 

#Merge two dictionaries
def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
print(merge_dicts(a, b))   


# #Frequency of each character in a string
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
print(char_frequency("programming"))

# #Implement custom max()
def my_max(iterable):
    if not iterable:
        raise ValueError("Empty iterable")
    maximum = iterable[0]
    for item in iterable[1:]:
        if item > maximum:
            maximum = item
    return maximum
nums = [10, 45, 23, 67, 89, 12]
print(my_max(nums))   


#Lists, Strings & Collections
#Reverse a list **in place** without using `[::-1]` or `reverse()`.
def reverse_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst
print(reverse_list([2, 3, 7, 6, 5]))  

#Flatten a nested list
def flatten_list(nested):
    flat = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    return flat
print(flatten_list([[1, 2], [3, 4], [5, 6]]))  

#Count vowels and consonants in a string
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = c_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count
v, c = count_vowels_consonants("Saadwitha")
print("Vowels:", v, "Consonants:", c)  

#Find the second largest number in a list
def second_largest(nums):
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None
print(second_largest([10, 20, 4, 55, 99]))  

#Rotate a list by k elements (circular shift)
def rotate_list(lst, k):
    n = len(lst)
    k = k % n   
    return lst[-k:] + lst[:-k]
print(rotate_list([1, 2, 3, 4, 5], 2)) 

#Iterators & Generators
#Custom iterator for square numbers up to n
class SquareIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.n:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration
for sq in SquareIterator(10):
    print(sq, end=" ")  

#Generator function for even numbers up to n
def even_numbers(n):
    for i in range(2, n+1, 2):
        yield i
print(list(even_numbers(20))) 

#Fibonacci generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fibonacci(8)))  

#Generator to read a large file line by line
def read_large_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()
for line in read_large_file("sample.txt"):
    print(line)

#Prime number generator up to n
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_numbers(n):
    for i in range(2, n+1):
        if is_prime(i):
            yield i
print(list(prime_numbers(30)))  

#Functions
#Function with *args and **kwargs
def print_args_kwargs(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword Arguments:", kwargs)
print_args_kwargs(1, 2, 3, name="Alice", age=25)

#Recursive factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  

#Recursive Fibonacci function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print([fibonacci(i) for i in range(7)]) 

#Return list with only unique elements
def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
print(unique_list([1, 2, 2, 3, 4, 4, 5]))  

#Sum of digits of a number
def sum_of_digits(num):
    total = 0
    for digit in str(abs(num)):
        total += int(digit)
    return total
print(sum_of_digits(1234))  
