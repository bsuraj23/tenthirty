#  . Implement a safe file reader that handles `FileNotFoundError`.

def safe_file_reader(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    finally:
        print("File read attempt completed.")


# Example usage
data = safe_file_reader("sample.txt")
if data is not None:
    print("File content:\n", data)

