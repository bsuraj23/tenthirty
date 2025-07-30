chars = ['a', 'b', 'c', 'a', 'b', 'a']

# Create an empty dictionary to count characters
count_dict = {}

# Count each character
for ch in chars:
    if ch in count_dict:
        count_dict[ch] += 1
    else:
        count_dict[ch] = 1

# Find the character with maximum count
max_char = None
max_count = 0

for key in count_dict:
    if count_dict[key] > max_count:
        max_count = count_dict[key]
        max_char = key

# Output
print(f"Most common character: {max_char} (repeated {max_count} times)")
