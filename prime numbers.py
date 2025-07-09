number=int(input("Enter the number: "))
if number>1:
    for i in range(2,number):
        if number%i==0:
            print(number,"Not a prime")
            break   
    else:
        print(number,"Is prime")
        
else:
    print(number,"Not a prime")