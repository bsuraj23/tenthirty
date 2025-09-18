import os
from contextlib import contextmanager

@contextmanager
def change_directory(new_path):
    original_path = os.getcwd()
    os.chdir(new_path)
    try:
        yield
    finally:
        os.chdir(original_path)
        print(f"Returned to original directory: {original_path}")

# Example usage
import os

print("Current directory:", os.getcwd())

with change_directory("/tmp"):
    print("Inside context, current directory:", os.getcwd())

print("Outside context, current directory:", os.getcwd())
