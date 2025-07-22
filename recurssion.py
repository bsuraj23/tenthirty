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
       




