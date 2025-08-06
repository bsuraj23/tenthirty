In Python, the documentation of a function is provided using a docstring—a string literal placed immediately after the function definition, enclosed in triple quotes ("""..."""). The docstring describes what the function does, and can include details about the function’s arguments, return values, exceptions, and usage examples.
A good function docstring typically starts with a brief summary on the first line, optionally followed by more detailed information, including parameter and return value descriptions if needed. For example:

program:

def sum_subtract(a, b, operation="sum"):
    """
    Return sum or difference between the numbers 'a' and 'b'.

    The type of operation is defined by the 'operation' argument.
    If the operation is not supported, print 'Incorrect operation.'
    """
    if operation == "sum":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        print("Incorrect operation.")
You can access a function's documentation at runtime using the function’s doc attribute or through the help() function. There are several accepted conventions for structuring docstrings (such as Google, NumPy, and reStructuredText styles), but all aim to make the function’s purpose and behavior clear.

