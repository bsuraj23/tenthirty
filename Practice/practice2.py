#RECURSSION

#Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * (n-1)
print (factorial(3))


#Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print (fibonacci(8))


#Sum of Number
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n-1)
print(sum_numbers(10))

#Reverse String
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:])+ s[0]
print(reverse_string('ihtpeeD'))


#Power of a number
def power(base,exp):
    if exp == 0:
        return 1
    return base * power(base,exp-1)
print(power(3,2))

#Find max element in a list
def find_max(lst):
    if len(lst)==1:
        return lst[0]
    return max(lst[0],find_max(lst[1:]))
print(find_max([2,8,1,5,0,3]))


#Greatest common diviser (GCD)
def gcd(a,b):
    if b == 0:
        return a
    return gcd (b,a%b)
print(gcd(8,12))