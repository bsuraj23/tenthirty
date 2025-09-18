def count_words(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        return len(words)

# Example usage
filename = "sample.txt"
print(f"Number of words in {filename}:", count_words(filename))
