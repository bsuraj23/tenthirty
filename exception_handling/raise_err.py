# try:
#     raise ValueError("An error occurred")
# except ValueError as e:
#     print(f"Error: {e}")

try:
    raise RuntimeError("This is a runtime error")
except RuntimeError as e:
    print(f"Caught an error: {e}")