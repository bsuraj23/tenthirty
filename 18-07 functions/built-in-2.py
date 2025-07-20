def add ():
    a=90
    b=89
    c=a+b
    print(c)
add()  #calling function,defination



def check_locals():
    a=5
    b="text"
    print(locals())
check_locals()  #locals is used for dictionary key value pairs  to attach



def add(x, y):
    result = x + y
    print(result)
    print(locals())     #local is used for inside the function to attack every variable to key value pair
add(10,20)  




x = 100
print(globals()['x'])
globals()['new_var'] = 'created'
print(new_var)

def display_globals():
    print(list(globals().keys()))
display_globals()


