data = 'skgfuyvrtsugfsaduiuuhgvdhsahfshfisdh fchfusdifhuishfuhfscfugu'

freq = {}
for char in data:
    freq[char] = freq.get(char, 0) + 1

# Find max
most_common_char = max(freq, key=freq.get)
print(f"Most repeated character: '{most_common_char}' with count {freq[most_common_char]}")
