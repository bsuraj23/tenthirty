def greet(name):
    """
    Greet a person by their name.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    None
    """
    print("Hello, " + name + "!")

# Using the function
greet("Alice")

# To see the docstring of this function
print(greet.__doc__)