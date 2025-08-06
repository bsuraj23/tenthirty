n=int(input("Enter a number: "))
count=0
if n<=1:
    print("Not a prime number")
elif n == 2:
    print("Prime number")
else:
    for i in range(2,n):
        if n % i == 0:
            count+=1
            break
    if count == 0:
        print("Prime number ")
#it
    else:
        print("Not a prime number")