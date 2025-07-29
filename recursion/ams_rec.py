def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def armstrong_recursive(n, power):
    if n == 0:
        return 0
    digit = n % 10
    return (digit ** power) + armstrong_recursive(n // 10, power)

def is_armstrong(n):
    if n < 0:
        return "Invalid input"
    power = count_digits(n)
    if armstrong_recursive(n, power) == n:
        return f"{n} is an Armstrong number"
    else:
        return f"{n} is not an Armstrong number"

# Example:
print(is_armstrong(153))
