n = int(input("Enter a number: "))
a=1
b=2
while n > 0:
    c=a+b
    a=b
    b=c
    n-=1
    print(c)