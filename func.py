def square(number):
    """
    Calculates the square of a number.

    Parameters:
    number (int or float): The number to be squared

    Returns:
    int or float: The square of the input number
    """
    return number * number

# Calling the function
result = square(5)
print("Square is:", result)

# Displaying the documentation
print("\nFunction Documentation:")
print(square.__doc__)
