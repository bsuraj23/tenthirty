n=int(input("Enter range: "))
for i in range(1,n+1):
    for j in range(i):
        if(i+j)%2==0:
            print("1", end="")
        else:
            print("0", end="") 
    print()# Move to the next line after each row  
