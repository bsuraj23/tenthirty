#custom iterator class - squares upto n

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
        
for num in SquareIterator(5):
    print(num)

#Fibonacci number using generator
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a+b

for num1 in fibonacci(20):
    print(num1)

# Read a large file line by line using generator

#for thi we should create a text file and copy that file path and replace that instead of file_path in the code.
def read_large_file(file_path):
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()


#prime numbers upto n using generators
def primes_up_to(n):
    for num in range(2, n+a):
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                break
        else:
            yield num
for prime in primes_up_to(20):
    print(prime)
    
 