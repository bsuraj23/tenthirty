#Namespaces & Scope

#Function demonstrating the LEGB rule with nested functions
x = "global"  
def outer():
    x = "enclosing"  
    def inner():
        x = "local"  
        print("LEGB rule picks:", x) 

    inner()
outer()
print("From global scope:", x)

#Function that modifies a global variable using global
count = 0   
def increment():
    global count
    count += 1
increment()
increment()
print("Global count =", count)  

#Function that modifies an enclosed variable using nonlocal
def outer():
    x = 10   
    def inner():
        nonlocal x
        x += 5
        print("Inner x =", x)
    inner()
    print("Outer x after inner call =", x)
outer()

#Function with variable shadowing a built-in (sum)

def bad_function():
    sum = 100
    print("Shadowed sum =", sum)
def good_function():
    numbers = [1, 2, 3]
    result = sum(numbers)   
    print("Correct sum =", result)
bad_function()
good_function()

#Demonstrate name collisions between global and local variables
x = "global x"
def my_func():
    x = "local x"
    print("Inside function:", x)
my_func()
print("Outside function:", x)