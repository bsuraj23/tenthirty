import re

print(re.split(r'\s+','This is a test string.'))
print(re.split(r'\d+','abc123xyz'))
print(re.split(r'[:,]','apple,banana:orange'))
print(re.split(r'[A-Z]','i amHelloWorld'))