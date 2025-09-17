# Reverse a string ( Without Slicing)
s = "Deepthi"
result = ""
for ch in s:
    result = ch + result
print(result)


#Find the largest number in a list.
numbers = [12, 45, 78, 34, 89, 23]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("The largest number is:", largest)


# Count vowels in a string
v = "Deepthi"
vowels = "aeiouAEIOU"
count = 0
for ch in v:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)


#Write a program to check if a number is prime
num = int(input("Enter a number: "))
if num < 2:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

#Custom iterator for fibonacci numbers
class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit  
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self  

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration  
        value = self.a
        self.a, self.b = self.b, self.a + self.b  
        self.count += 1
        return value

fib = FibonacciIterator(10)
for num in fib:
    print(num)

#Function decorator to log execution time
import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@log_execution_time
def slow_function():
    total = 0
    for i in range(1_000_000):
        total += i
    return total

print(slow_function())

# generator for even numbers upto n
def even_numbers(n):
    for i in range(0, n+1, 2):
        yield i  # yield instead of return
for num in even_numbers(10):
    print(num)

#Flatten a nested list
def flatten_list(nested_list):
    flat = []
    for sublist in nested_list:
        for item in sublist:
            flat.append(item)
    return flat
print(flatten_list([[1, 2], [3, 4], [5, 6]]))

#Read a Text File and Count Word Frequencies
def count_word_frequencies(filename):
    word_count = {}
    with open(filename, "r") as file:
        text = file.read().lower()  
        words = text.split()  
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

# We should have a text file named 'sample.txt'.
print(count_word_frequencies("sample.txt"))

#Custom Context manager for file operations
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file  

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close() 

with FileManager("myfile.txt", "w") as f:
    f.write("Hello, this is written using a context manager!")

with FileManager("myfile.txt", "r") as f:
    print(f.read())

#use map and filter to get squares of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x ** 2, evens)
print(list(squares))  


#Custom module and a call function
# -> First we should create a mymodule.py
def greet(name):
    return f"Hello, {name}!"
#->Next we should create a mail file - main.py
import mymodule  
print(mymodule.greet("Deepthi"))
#->now run it by making sure that both .py files are in the same folder

#Serialize & Deserialize a dictionary with JSON
import json
data = {"name": "Alice", "age": 25, "city": "Hyderabad"}
json_string = json.dumps(data)
print("Serialized JSON:", json_string)
new_data = json.loads(json_string)
print("Deserialized Dictionary:", new_data)

#Read command line arguments with argparse
import argparse
def main():
    parser = argparse.ArgumentParser(description="Add two numbers from command line")
    parser.add_argument("num1", type=int, help="First number")
    parser.add_argument("num2", type=int, help="Second number")
    args = parser.parse_args()

    result = args.num1 + args.num2
    print(f"The sum is: {result}")

if __name__ == "__main__":
    main()

    














