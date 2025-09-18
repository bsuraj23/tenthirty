#51.What is a closure in Python? How is it different from a normal function?
def outer_function(x):
    def inner_function(y):
        return x + y  # inner function "remembers" x from outer scope
    return inner_function

# Create a closure
add_five = outer_function(5)

# Call the inner function
print(add_five(10))  # Output: 15
print(add_five(3))   # Output: 8
