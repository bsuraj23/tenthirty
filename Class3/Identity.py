print("Identity opertors are IS and Is not ")
a = "I am a"
b = "I am b"
c = 90
print(type(a))
print(type(b))
print("a is b", a is b)
print("a is not b", a is not b)
print("a is c", a is c)
print("b is c", b is c)
age = 15
citizen = 12
if (age>= 18):
    print("Eligible for voting ")
    if(citizen is  1):
        print("And check if Indian then only voting      ")
    else:
        print("not a citizen so even if more than 18 no voting    NOT Eligible for voting    ")

        

else:
    print("NOT Eligible for voting ")

