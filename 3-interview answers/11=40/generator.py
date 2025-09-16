#  Write a generator that reads a large file line by line.
def read_large_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()   # strip removes newline characters


# Example usage
for line in read_large_file("sample.txt"):
    print(line)
