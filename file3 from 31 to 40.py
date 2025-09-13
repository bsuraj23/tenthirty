#Exception Handling
#31. Write code to handle division by zero with try-except.
try:
    a = 10
    b = 0
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

#32. Create a custom exception `NegativeNumberError` and raise it when a negative number is passed.
class NegativeNumberError(Exception):
    pass
def check_number(num):
    if num < 0:
        raise NegativeNumberError(f"Negative number {num} not allowed")
    print(num, "is valid")
try:
    check_number(-3)
except NegativeNumberError as e:
    print(e)
#33. Implement a function that retries division 3 times if an error occurs.
def safe_division(a, b, retries=3):
    for attempt in range(1, retries + 1):
        try:
            result = a / b
            print(f"Result: {result}")
            return result
        except ZeroDivisionError:
            print(f"Attempt {attempt}: Cannot divide by zero!")
            if attempt == retries:
                print("All retries failed.")
                return None
safe_division(10, 0)

#34. Write code that handles multiple exceptions (e.g., `ZeroDivisionError`, `ValueError`).
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("Result:", a / b)
except (ZeroDivisionError, ValueError) as e:
    print("Error:", e)
#35. Implement a safe file reader that handles `FileNotFoundError`.
def safe_file_reader(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
safe_file_reader("example.txt")

# Decorators & Context Managers
#36. Write a decorator that logs the execution time of a function.
import time
def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper
@log_time
def example():
    time.sleep(1)
example()

#37. Implement a decorator that counts how many times a function is called.
def count_calls(func):
    func.calls = 0
    def wrapper(*args, **kwargs):
        func.calls += 1
        print(f"{func.__name__} called {func.calls} times")
        return func(*args, **kwargs)
    return wrapper
@count_calls
def greet():
    print("Hello!")
greet()
greet()
greet()

#38. Write a decorator that only allows function execution if the user is "admin".
def admin_only(func):
    def wrapper(user, *args, **kwargs):
        if user == "admin":
            return func(user, *args, **kwargs)
        else:
            print("Access denied: Admins only")
    return wrapper
@admin_only
def secure_task(user):
    print("Task executed!")
secure_task("admin")  # Executes
secure_task("guest")  # Denied

#39.Create a context manager that opens a file and automatically closes it
from contextlib import contextmanager
@contextmanager
def open_file(file_name, mode):
    f = open(file_name, mode)
    try:
        yield f
    finally:
        f.close()
with open_file('example.txt', 'w') as file:
    file.write("Hello, world!")

# .40. Write a context manager that temporarily changes the working directory.
import os
from contextlib import contextmanager
@contextmanager
def change_dir(destination):
    original_dir = os.getcwd()
    os.chdir(destination)
    try:
        yield
    finally:
        os.chdir(original_dir)
with change_dir('/path/to/dir'):
    print("Current directory:", os.getcwd())
print("Back to original directory:", os.getcwd())


