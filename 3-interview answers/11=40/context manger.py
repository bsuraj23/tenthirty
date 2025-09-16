from contextlib import contextmanager

@contextmanager
def open_file(file_path, mode):
    file = open(file_path, mode)
    try:
        yield file  # provide the file object
    finally:
        file.close()
        print(f"File '{file_path}' has been closed.")

# Example usage
with open_file("example.txt", "w") as f:
    f.write("Hello, world!")
