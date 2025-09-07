# locals()


def add ():
    a=50
    b=40
    c=a+b
    print(c)
add()  

def check_locals():
    a = 5
    b = "text"
    print(locals())

check_locals()

def add(x, y):
    result = x + y
    print(result)
    print(locals())

add(50, 40)

# # globals()
x = 10
print(globals()['x'])

globals()['new_var'] = 'newcreated'
print(new_var)

def display_globals():
    print(list(globals().keys()))

display_globals()