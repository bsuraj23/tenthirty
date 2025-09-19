class Demo:
    def __init__(self, p1, p2, p3, p4):
        print("Inside __init__")
        print("p1:", p1)
        print("p2:", p2)
        print("p3:", p3)
        print("p4:", p4)

# Call with positional arguments (order matters)
obj1 = Demo(10, 20, 30, 40)

# Call with keyword arguments (order does not matter)
obj2 = Demo(p4=400, p2=200, p1=100, p3=300)