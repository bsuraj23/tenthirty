import re
m = re.search(r'(\d{3})-(\d{2})-(\d{4})', '123-45-6789')
print(m.group(1), m.group(2), m.group(3))
m = re.search(r'(\w+) (\w+)', 'Hello World')
print(m.group(0),m.group(1), m.group(2))
m = re.match(r'(abc)(\d+)', 'abc123')
print(m.group(1), m.group(2))
m = re.search(r'(Hi|Hello) (\w+)', 'Hello John')
print(m.group(1), m.group(2))
m = re.search(r'(colou?r)', 'color')
print(m.group(1))
m = re.search(r'(start).*(middle).*(end)', 'start middle end')
print(m.group(1), m.group(2),m.group(3))
m = re.search(r'(\d{2}):(\d{2})', '12:30 PM')
print(m.group(1), m.group(2))



print(re.sub(r'\d+', 'X', 'Item 123 costs 456'))
print(re.sub(r'cat', 'dog', 'The cat sat on the mat'))
print(re.sub(r'\s+', '-', 'replace spaces with dash'))
print(re.sub(r'[^a-zA-Z0-9]', '', 'Remove@#Special!'))
print(re.sub(r'_', ' ', 'split_this_string'))
print(re.sub(r'(.)(?=\1)', '', 'aabbcc'))  # Remove consecutive duplicates
print(re.sub(r'^', 'Start-', 'line is not there'))


print(re.findall(r'\d+', 'There are 3 cats and 4 dogs'))
print(re.findall(r'[A-Z]', 'Python Is Great'))
print(re.findall(r'colou?r', 'color and colour'))
print(re.findall(r'\b\w{4}\b', 'This text has four word size words'))
print(re.findall(r'\s', 'space here and there'))
print(re.findall(r'\w+', 'List all words here123'))
print(re.findall(r'[aeiou]', 'Count vowels in sentence'))