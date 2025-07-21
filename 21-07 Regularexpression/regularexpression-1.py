import re
print(re.match(r'\d+', '743abc'))
print(re.match(r'\w+','123abc'))
print(re.match(r'\d+','abc'))
print(re.match(r'[a-z]+','abc'))
print(re.match(r'[A-Z]\w+','AbC'))
print(re.match(r'Harish','Harish where are you'))
print(re.match(r'^\d', '5'))
print(re.match(r'.+', 'AnyTextHere ^^^^*&(%)$3232'))


