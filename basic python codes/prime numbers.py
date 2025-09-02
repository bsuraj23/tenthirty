n=int(input())
if n<2:
    print("Not prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("Prime")