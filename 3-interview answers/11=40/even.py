# Write a generator function that yields even numbers up to `n`.
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


# Example usage
for num in even_numbers(10):
    print(num)
