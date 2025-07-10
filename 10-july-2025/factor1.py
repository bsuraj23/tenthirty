import math

n = int(input(("enter your number: \n")))

print("square is",math.sqrt(n))
x = int(input("write a number2: \n"))
print("power is",math.pow(x,n))
print("log is",math.log(n))
print("exp is",math.exp(n))

f = float(input("enter the floating number: \n"))
print(math.floor(f))
print(math.ceil(f))
print(math.fabs(f)) # changes into positive
print("fact is "math.factorial(n))