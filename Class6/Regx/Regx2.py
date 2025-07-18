import re

print(re.search(r'\d+', 'abc123xyz'))
print(re.search(r'cat', 'The black cat is here.'))
print(re.search(r'[A-Z]+', 'helloWorldTest'))
print(re.search(r'end$', 'This is the end'))
print(re.search(r'^\w+', 'Start123 end'))
print(re.search(r'colou?r', 'The color is nice'))
print(re.search(r'\s', 'space here'))
