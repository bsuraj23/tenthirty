#Functions
#16.*args and **kwargs
def demo(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)
demo(1, 2, 3, a=10, b=20)
#17.Recursive factorial
def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)
print(fact(5))
#18.Recursive fibanocci
def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)
print([fib_rec(i) for i in range(8)])
#19.Unique list preserving order
def unique(lst):
    return list(dict.fromkeys(lst))
print(unique([1, 2, 2, 3, 1, 4]))
#20.Sum of digits of a number
def sum_digits(n):
    return sum(int(d) for d in str(n))
print(sum_digits(12345))