#  Create a generator that yields prime numbers up to `n`.
def prime_generator(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for number in range(2, n + 1):
        if is_prime(number):
            yield number


# Example usage
for prime in prime_generator(30):
    print(prime)
