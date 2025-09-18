#Iterators & Generators

#Create a custom iterator class that generates square numbers up to n
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

squares = SquareIterator(5)
for num in squares:
    print(num)  

#Write a generator function that yields even numbers up to n
def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

for num in even_numbers(10):
    print(num, end=" ")  

#Implement a generator that yields Fibonacci numbers
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num, end=" ")  

#Write a generator that reads a large file line by line
def read_large_file(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()
# create "data.txt" before running:
for line in read_large_file("data.txt"):
    print(line)

#Create a generator that yields prime numbers up to n
def prime_numbers(n):
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

for p in prime_numbers(30):
    print(p, end=" ") 
