def add(a,b):
    return a+b
print(add(3,3))

#multliplication
print("Multliplication")
def multiply(a=5,b=5):
    return a*b
print(multiply(4,4))


#even 
print("Printing is_even")
def is_even(num):
    return num % 2==0
print(is_even(12))

#printing msg
print("printing msg")
def message(msg):
    return msg
print(message(81))


#importing math
import math
def squareroot(num):
    result=math.sqrt(num)
    return result
num=25
print(num,"is",squareroot(num))


