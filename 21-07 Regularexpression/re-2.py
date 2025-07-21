import re

print(re.search(r'\d+', 'abc123xyz567'))
print(re.search(r'cat', 'The black cat is here.'))
print(re.search(r'[A-Z]+', 'helloWorldTest'))
print(re.search(r'the start$', 'This is the start'))
print(re.search(r'^\w+', 'Start123 end'))
print(re.search(r'colour', 'The colour is nice'))
print(re.search(r'\s', 'space here'))
