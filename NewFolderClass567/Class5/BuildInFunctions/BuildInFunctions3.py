# locals()


# def add ():
#     a=90
#     b=89
#     c=a+b
#     print(c)
# add()  #calling function,defination


# def check_locals():
#     a = 5
#     b = "text"
#     print(locals())

# check_locals()

# def add(x, y):
#     result = x + y
#     print(result)
#     print(locals())

# add(10, 20)

# # globals()
x = 100
print(globals()['x'])

globals()['new_var'] = 'created'
print(new_var)

def display_globals():
    print(list(globals().keys()))

display_globals()
