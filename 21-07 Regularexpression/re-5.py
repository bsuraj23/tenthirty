import re

matches = re.finditer(r'\d+', 'Item 1 costs 20 and 30 more')
for m in matches:
    print(m.group())

matches = re.finditer(r'\w+', 'List all words here')
for m in matches:
    print(m.group())

matches = re.finditer(r'[A-Z]', 'Python Is PowerfuL')
for m in matches:
    print(m.group())

matches = re.finditer(r'colou?r', 'color or colour appears twice')
for m in matches:
    print(m.group())

matches = re.finditer(r'\b\w{3}\b', 'One two red blue')
for m in matches:
    print(m.group())

matches = re.finditer(r'\s', 'Multiple spaces exist here')
for m in matches:
    print('Space found at:', m.start())

matches = re.finditer(r'\d{2}', '12 34 56 7856')
for m in matches:
    print(m.group())



pattern = re.escape('a+b*c')
print(re.match(pattern, 'a+b*c'))

pattern = re.escape('1.5$')
print(re.match(pattern, '1.5$'))

pattern = re.escape('[a-z]+')
print(re.match(pattern, '[a-z]+'))

pattern = re.escape('(group)')
print(re.match(pattern, '(group)'))

pattern = re.escape('{1,3}')
print(re.match(pattern, '{1,3}'))

pattern = re.escape('special^chars$')
print(re.match(pattern, 'special^chars$'))

pattern = re.escape('^start')
print(re.match(pattern, '^start'))

print(re.findall(r'^Hello', 'Hello there!'))
print(re.findall(r'\D+', 'Only words and spaces 123'))
print(re.findall(r'\d+', 'Find 123 and 456'))
print(re.findall(r'\D+', 'Only words and spaces 123'))
print(re.findall(r'\s+', 'Spaces are \t included \n here'))
print(re.findall(r'\S+', 'Non-space characters only'))
print(re.findall(r'\w+', 'Words_and123numbers'))
print(re.findall(r'\W+', '!!@@##$$ symbols only'))
print(re.findall(r'^Hello', 'Hello there!'))
