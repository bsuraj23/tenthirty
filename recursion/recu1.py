def fac(n):
    while n > 1:
        return n * fac(n - 1)
    return 1
print(fac(5))