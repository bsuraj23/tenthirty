n=int(input("Elnter the number:"))
a=0
b=1
print(a)
print(b)
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c)