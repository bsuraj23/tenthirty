#context manager for filr operations
class MyFile:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Usage
with MyFile('file.txt', 'r') as file:
    print(file.read())