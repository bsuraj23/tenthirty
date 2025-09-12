#count word frequencies in a file
from collections import Counter
import os
file_path = 'file.txt'
if not os.path.exists(file_path):
    print(f"Error: {file_path} not found.")
else:
    with open(file_path) as f:
        words = f.read().split()
    freq = Counter(words)
    for word, count in freq.items():
        print(f"{word}: {count}")