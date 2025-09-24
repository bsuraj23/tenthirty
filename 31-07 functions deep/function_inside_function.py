def outer():
    def inner():
        return "Hello from inner!"
    return inner   # returning the function itself, not calling it

func = outer()
print(func())   # calling the returned function
