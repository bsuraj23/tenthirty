
from collections import Counter

def most_common_repeated_char(char_arrays):
    # Flatten all arrays into one list of characters
    all_chars = []
    for array in char_arrays:
        all_chars.extend(array)

    # Count frequency of each character
    char_counts = Counter(all_chars)

    # Filter to keep only repeated characters (count > 1)
    repeated_chars = {char: count for char, count in char_counts.items() if count > 1}

    # Find the character with the highest count
    if repeated_chars:
        most_common_char = max(repeated_chars.items(), key=lambda item: item[1])
        return most_common_char[0], most_common_char[1]
    else:
        return None, 0

# Example usage
char_arrays = [
    ['a', 'b', 'c'],
    ['b', 'c', 'd'],
    ['e', 'f', 'c']
]

char, count = most_common_repeated_char(char_arrays)
if char:
    print(f"Most common repeated character is '{char}' with {count} occurrences.")
else:
    print("No repeated characters found.")
