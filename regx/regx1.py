import re

print(re.match(r'\d+', 'r123abc'))
print(re.match(r'\w+', 'Hello123'))
print(re.match(r'[A-Z]\w+', 'Python3'))
print(re.match(r'[a-z]+', 'abcXYZ'))
print(re.match(r'abc', 'abcde'))
print(re.match(r'^\d', '5days'))
print(re.match(r'.+', 'AnyTextHere'))