from collections import Counter


text = input()

count = Counter(text)
print(count)
print(count.most_common(1))
