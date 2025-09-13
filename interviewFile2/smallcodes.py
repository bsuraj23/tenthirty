x=15
def abc(a):
    a= a+15
                 #immutable does not changes
abc(x)
print(x)    

lst=[1,2,3,4]
def change(x):
    x.append(5)
                     #mutable
change (lst)
print(lst)    

#function assign to variable

def square(x):
    return x*x

s=square
print(s(5))

#lambda functions
add= (lambda x,y : x+y)
sqr = (lambda x: x**2)

print(add(3,4))
print(sqr(7))