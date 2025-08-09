#print numbers from 1 to 10,but skip number 5
for i in range(1,11):
    if i==5:
        continue
    #skip multiples of 3
    i=0
    while i<10:
        i+=1
        if i%3==0:
            continue
        print(i)

#demonstrate use of pass inside loop
for i in range(1,6):
    if i==3:
        pass
    print(i)
    #using pass in an if statement
    x=10
    if x>5:\
    pass
else:
    print("x is 5 or less")