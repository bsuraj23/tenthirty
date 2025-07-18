# Function Object - 6 Examples

# Example 1
def simple_func():
    print("Hello!")

print(simple_func)

# Example 2
def adder(x, y):
    return x + y

print(type(adder))

# Example 3
print(adder)

# Example 4
func_ref = adder
print(func_ref(5, 10))

# Example 5
def multiply_func(a, b):
    return a * b

print(multiply_func)

# Example 6
def greet():
    print("Hello from greet!")

print(globals()['greet'])
