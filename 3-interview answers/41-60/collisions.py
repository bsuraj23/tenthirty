x = 100  # global variable

def demo_collision():
    x = 50   # local variable shadows global x
    print("Inside function, x =", x)

demo_collision()
print("In global scope, x =", x)
