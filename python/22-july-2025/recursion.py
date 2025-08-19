# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))

# # def add(a,b): 
# #     return a + b


# # print(add(3,4))


# def magic_box(x):
#     return x * 2

# x = int(input())
# print(magic_box(x))


# Fibonacci sequence using recursion

def fib(n):
    if n <= 1:
        return n 
    return fib(n-1) + fib(n-2)

print(fib(6))
