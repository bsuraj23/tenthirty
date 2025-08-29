from collections import Counter

# Input string or character array
data = "programming"

# Count character frequencies
counter = Counter(data)

# Get the most common character
most_common_char, count = counter.most_common(1)[0]

print(f"The most common character is '{most_common_char}' which appears {count} times.")
