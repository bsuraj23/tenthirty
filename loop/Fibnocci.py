n = int(input("Enter range: "))
a=0
b=1
print("Fibonacci series:", a, b, end=" ")
while n > 0:
    c=a+b
    a=b
    b=c
    n-=1
    print(c, end=" ")
#print("Fibonacci series:", a,b,c)