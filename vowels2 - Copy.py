#Coding Practice (Beginner)
#Count vowels in a string.
s='padamati swathi'
vowels='aeiou'
count=0
for ch in s:
  if ch in vowels:
    count += 1
print(count)
