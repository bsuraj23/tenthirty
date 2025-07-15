arr=[1,2,3,4,5,6,23]
up=arr[-1]
lo=arr[0]
for i in range(lo, up+1):
    count=0
    for j in range(1,i+1):
        if (i%j==0):
            count+=1
    if count == 2:
        print(i, "is a prime number")
        