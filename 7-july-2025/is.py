x = "x is x"
y = "y is y"
z = 44

print(type(x))
print(type(y))
print(type(z))

#Usage of is function 
if x is x:
    print("it is x")
    #Nested loop
    if x is not y:
        print("It is not equal to y")
else:
    print("it's not a x")

if x is not x:
    print("It is not equal")
else:
    print("It is x")

print(z)



#7july2025