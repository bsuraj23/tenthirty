def add(a,b):
    return a+b
print(add(5,14))

#multliplication
print("Multliplication")
def multiply(a=5,b=14):
    return a*b
print(multiply(5,14))


#Odd 
print("Printing is_odd")
def is_odd(num):
    return num % 1==0

# Even num
print("Printing is_even")
def is_even(num):
    return num % 2==0
print(is_even(6))

#printing msg
print("printing msg")
def message(msg):
    return msg
print(message(81))


# Importing math
import math
def squareroot(num):
    result=math.sqrt(num)
    return result
num=49
print(num,"is",squareroot(num))