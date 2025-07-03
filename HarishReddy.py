#Arithmetic Operations using
a=float(input("Enter first number : "))
b=float(input("Enter second number : "))
print("Choose operator: +, -, *, /")
op=input("Enter operator:")
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    if b !=0:
        print(a/b)
    else:
        print("Error: Cannot divide by Zero")
else:
    print("Invalid Operator input")




#Logical Operations 
c=int(input("Enter first number:"))
d=int(input("Enter second number:"))
if c>0 and d>0:
    print("Both are positive numbers")
if c>0 or d>0:
    print("Atleast one number is positive")
if not (c<0):
    print("First number is not negative")
    
