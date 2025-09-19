# Data Handling & Error Management
#Write code to read a text file and count word frequencies.
from collections import Counter
def count_word_frequencies(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()   # read and convert to lowercase
    words = text.split()
    word_counts = Counter(words)
    return word_counts
if __name__ == "__main__":
    filename = "sample.txt"   
    counts = count_word_frequencies(filename)
for word, freq in counts.items():
        print(f"{word}: {freq}")


#Write a **context manager** to handle file operations.
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file   
    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        if self.file:
            self.file.close()
        return False
with FileManager("sample.txt", "w") as f:
    f.write("Hello from custom context manager!\n")


#Use `map` and `filter` to get squares of even numbers from a list.
# filter(lambda x: x % 2 == 0, numbers) → keeps only even numbers.
# map(lambda x: x ** 2, ...) → squares each filtered number.
#Sample list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_evens = list(
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))  #squares of even numbers
)
print(squares_of_evens)


#Serialize and Deserialize a Python dictionary using JSON
import json
data = {"name": "Alice", "age": 25, "is_student": False}
json_str = json.dumps(data)
print("Serialized:", json_str)
parsed_data = json.loads(json_str)
print("Deserialized:", parsed_data)


#Script to read command line arguments with argparse
import argparse
parser = argparse.ArgumentParser(description="A simple argparse demo")
parser.add_argument("--name", type=str, help="Your name")
parser.add_argument("--age", type=int, help="Your age")
args = parser.parse_args()
print(f"Hello {args.name}, you are {args.age} years old!")
