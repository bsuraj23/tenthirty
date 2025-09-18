def primes_upto(n):
    primes = []
    for num in range(2, n + 1):       # start from 2 (smallest prime)
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # check up to √num
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Example usage
n = int(input("Enter n: "))
print("Prime numbers up to", n, "are:", primes_upto(n))
