def outer():
    x = 10  # enclosed variable

    def inner():
        nonlocal x
        x += 5
        print("Inside inner(), x =", x)

    inner()
    print("Inside outer(), x =", x)

outer()
