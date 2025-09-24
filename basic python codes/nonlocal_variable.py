def outer():
    x=10
    def inner():
        nonlocal x
        x=20
        print("Inner:",x)
    inner()
    print("Outer",x)
outer()
# print(x)  here x is not defined if you run this code