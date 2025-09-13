#Namespaces & Scope
#46.LEGB rule (Local — Enclosing — Global — Builtins)
GLOBAL = "global value"

def outer():
    ENC = "enclosing value"
    def inner():
        LOC = "local value"
        print("local:", LOC)
        print("enclosing:", ENC)
        print("global:", GLOBAL)
        print("builtin len used on [1,2,3]:", len([1,2,3]))
    inner()

outer()
#47.global keyword (modify a global variable inside a function)
counter = 0

def increment():
    global counter
    counter += 1

print("before:", counter)
increment()
print("after:", counter)
#48.nonlocal keyword (modify a variable from the enclosing scope)
def outer():
    n = 0
    def inner():
        nonlocal n
        n += 1
        return n
    print(inner())  
    print(inner())  

outer()
#49.Shadowing built-in sum (why it’s a problem and how to fix)
# Problem: shadow the built-in name `sum`
sum = 0
for i in [1, 2, 3]:
    sum += i
print("sum variable:", sum)

# Now delete the local/global variable to restore access to the builtin
del sum
print("built-in sum works again:", sum([1, 2, 3]))
#50.Name collisions: local variable shadows a global variable
message = "global message"

def show():
    message = "local message"   # this local name shadows global `message`
    print("inside show():", message)

print("before show():", message)
show()
print("after show():", message)