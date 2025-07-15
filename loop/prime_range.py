a=int(input("Enter your lower: "))
n=int(input("Enter a upper: "))
for i in range(a, n+1):
    count=0
    for j in range(1, i+1):
        if (i%j==0):
            count+=1
    if count == 2:
        print(i, "is a prime number")

            

