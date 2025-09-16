from functools import wraps

def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Function '{func.__name__}' has been called {wrapper.count} times")
        return func(*args, **kwargs)
    wrapper.count = 0  # initialize counter
    return wrapper


# Example usage
@call_counter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")
