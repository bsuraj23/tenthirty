#Write a function that takes \*args and \*\*kwargs and prints them separately.
def print_args_kwargs(*args, **kwargs):
    print("Positional arguments (*args):")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Example usage
print_args_kwargs(10, 20, 30, name="Alice", age=25, city="New York")
