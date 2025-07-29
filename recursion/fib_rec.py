# def fib(n):
#     if n < 0:
#         return "Invalid input"
#     elif n == 0:
#         return 0
#     elif n<=1:
#         return n
#     return fib(n-1) + fib(n-2)
# print(fib(6))  # Output: 5

def fib(n):
    if n <= 0:
        return "Invalid input"
    ser=[]
    a,b=0,1
    for i in range(n):
        ser.append(a)
        a,b=b,a+b
    return ser
print(fib(6))  # Output: [0, 1, 1, 2, 3, 5]
    