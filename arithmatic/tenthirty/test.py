#1.python code reverse your name
text="Archana"
print(text[::-1])


#2.factorial with without recursion
#3.difference between set and tuple
#Tuple:
#>tuple is denote with () "normal brackets
#>tuple is ordered
#>tuble is immutable
#Set:
#>set denote with {}"curly brackets
#>set is mutable
#>set is unordered
#>it collects unique elements
#features of python
#>it is high level language
#>easy to use and readability
#>it is used to web applications
#>gaming,datascience
#>it executes line by line,it is terprited

def factorial_recursive(n):
 if n==0:
  return 1
 else:
  return n * factorial_recursive(n-1)
num=int(input("enter a number"))
print("factorial(recursive):", factorial_recursive(num))

#factorial
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
print(fact(5))
#factorial with recursion(using loop)
def fact(n):
    result=1
    for i in range(1,n+1):
     result=result*i 
    return result
print(fact(5))
    
