#What are **functions** in Python? Difference between \*args and \*\*kwargs?

def function_name():
    add=20+30
    return add
print(function_name())

#args
def add_numbers(*args):  #here *args is a tuple 
    return sum(args)
print(add_numbers(1,2,3))

#kwargs
def print_details(**kwargs):    #here **kwarg stores as dictionary
    for key, value in kwargs.items():
        print(f"{key}:{value}")
    
print_details(name="Harish",age=21)
