from collections import Counter

# Sample array with 25 words (some repeated)
words = [
    "apple", "banana", "apple", "grape", "banana",
    "orange", "mango", "banana", "grape", "apple",
    "kiwi", "melon", "grape", "apple", "banana",
    "pear", "peach", "melon", "apple", "banana",
    "plum", "mango", "banana", "grape", "apple"
]

# Count word frequencies
word_count = Counter(words)

# Display all word counts
print("Word frequencies:")
for word, count in word_count.items():
    print(f"'{word}': {count}")

# Get most repeated word(s)
most_common = word_count.most_common(1)[0]
print(f"\nMost repeated word: '{most_common[0]}'")
print(f"Frequency: {most_common[1]}")


#output:
#Word frequencies:
#'apple': 6
#'banana': 6
#'grape': 4
#'orange': 1
#'mango': 2
#'kiwi': 1
#'melon': 2
#'pear': 1
#'peach': 1
#'plum': 1

#Most repeated word: 'apple'
#Frequency: 6
