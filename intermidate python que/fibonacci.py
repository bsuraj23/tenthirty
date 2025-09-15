class FibonacciIterator:
    def __init__(self):
        self.a, self.b = 0, 1   # first two Fibonacci numbers

    def __iter__(self):
        return self

    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b  # update for next time
        return value


# Using the infinite Fibonacci iterator
fib = FibonacciIterator()

for num in fib:
    if num > 10:   # stop when the number becomes greater than 50
        break
    print(num)
