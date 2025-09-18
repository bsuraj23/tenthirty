from collections import Counter
import re

#Extract words using regex
words = re.findall(r'\b\w+\b')

#Count frequencies
word_count = Counter(words)

#Print result
for word, freq in word_count.items:
 print(f"{word}:{freq}")
 
