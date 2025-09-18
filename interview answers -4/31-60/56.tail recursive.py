#56. How do you implement tail recursion optimization (since Python doesn’t have it natively)?
def fact(n, acc=1):
    if n == 0:
        return acc
    return fact(n - 1, acc * n)
