def factorial(n):
    if n==0:
       return 1
    else:
         return n*factorial(n-1)  
print(factorial(5))


#example of  fabonacci
def fabonacci(n):
    if n<=1:
       return n
    else:
        return fabonacci(n-1)+fabonacci(n-2)
print(fabonacci(6)) 

#example of sum of natural numbers
def sum_natural(n):
    if n==1:
       return 1
    else:
        return   n+sum_natural(n-1)
print(sum_natural(5))    

# Sum of numbers using recursion
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n-1)
print(sum_numbers(10))

# Reverse string using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]
print(reverse_string("python"))

# Power of a number using recursion
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
print(power(2, 4))

# Find max element in list using recursion
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], find_max(lst[1:]))
print(find_max([4, 7, 1, 9, 2]))

# GCD using recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(48, 18))

# reverse number
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)


num = 12345678910
reversed_num = reverse_number(num)
print("Reversed number:", reversed_num)

    
   


 




    












    











  
















    








