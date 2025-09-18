# Implement a generator that yields Fibonacci numbers.
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Example usage
for num in fibonacci_generator(10):
    print(num)
