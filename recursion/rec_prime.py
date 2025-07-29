# #Check prime or not using recursion
# def prime(n):
#     if n<=1:
#         return "Not a prime number"
#     for i in range(2,n+1):
#         if n % i == 0 and i != n:
#             return "Not a prime number"
#     return "Prime number"
# print(prime(5))  



#Check prime numbers in a range using iteration
n = 10

for num in range(2, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
