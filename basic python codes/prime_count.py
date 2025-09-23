n=int(input("Enter a number:"))
x=0
for num in range(2,n+1):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        x+=1
print(n,":",x)