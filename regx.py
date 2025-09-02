import re

print(re.match(r'\d+', '123abc'))
print(re.match(r'\w+', 'Hello123'))
print(re.match(r'[A-Z]\w+', 'Python3'))
print(re.match(r'[a-z]+', 'abcXYZ'))
print(re.match(r'abc', 'abcde'))
print(re.match(r'^\d', '5days'))
print(re.match(r'.+', 'AnyTextHere'))

# example 2
import re


print(re.search(r'\d+', 'abc123xyz'))
print(re.search(r'cat', 'The black cat is here.'))
print(re.search(r'[A-Z]+', 'helloWorldTest'))
print(re.search(r'end$', 'This is the end'))
print(re.search(r'^\w+', 'Start123 end'))
print(re.search(r'colou?r', 'The color is nice'))
print(re.search(r'\s', 'space here'))

# example 3
import re

pattern = re.compile(r'\d+')
print(pattern.match('123abc'))

pattern2 = re.compile(r'\w+')
print(pattern2.search('abc123'))

pattern3 = re.compile(r'^Hello')
print(pattern3.match('Hello World'))

pattern4 = re.compile(r'end$')
print(pattern4.search('This is the end'))

pattern5 = re.compile(r'[A-Z]{2,}')
print(pattern5.search('abCD123'))

pattern6 = re.compile(r'.+')
print(pattern6.match('SomeText'))

pattern7 = re.compile(r'^\d')
print(pattern7.match('9value'))

#example 4
import re

print(re.split(r'\s+', 'Split these words'))
print(re.split(r'\d+', 'item123price456'))
print(re.split(r'[:,]', 'apple,banana:cherry'))
print(re.split(r'[A-Z]', 'splitAtCapitals'))
print(re.split(r'_', 'split_this_string'))
print(re.split(r'-', '2025-07-15'))
print(re.split(r'\W+', 'Word1,Word2.Word3!'))

#example 5
import re

m = re.search(r'(\d{3})-(\d{2})-(\d{4})', '123-45-6789')
print(m.group(1), m.group(2), m.group(3))

m = re.search(r'(\w+) (\w+)', 'Hello World')
print(m.group(0), m.group(1), m.group(2))

m = re.match(r'(abc)(\d+)', 'abc123')
print(m.group(1), m.group(2))

m = re.search(r'(Hi|Hello) (\w+)', 'Hello John')
print(m.group(1), m.group(2))

m = re.search(r'(colou?r)', 'color')
print(m.group(1))

m = re.search(r'(start).*(end)', 'start middle end')
print(m.group(1), m.group(2))

m = re.search(r'(\d{2}):(\d{2})', '12:30 PM')
print(m.group(1), m.group(2))

#example 6
import re

print(re.fullmatch(r'\d+', '12345'))
print(re.fullmatch(r'\w+', 'Python3'))
print(re.fullmatch(r'abc', 'abc'))
print(re.fullmatch(r'[a-z]+', 'hello'))
print(re.fullmatch(r'[A-Z][a-z]+', 'Python'))
print(re.fullmatch(r'.+', 'JustText'))
print(re.fullmatch(r'colou?r', 'color'))


# example 7
import re
print(re.sub(r'\d+', 'X', 'Item 123 costs 456'))
print(re.sub(r'cat', 'dog', 'The cat sat on the mat'))
print(re.sub(r'\s+', '-', 'replace spaces with dash'))
print(re.sub(r'[^a-zA-Z0-9]', '', 'Remove@#Special!'))
print(re.sub(r'_', ' ', 'split_this_string'))
print(re.sub(r'(.)(?=\1)', '', 'aabbcc'))  # Remove consecutive duplicates
print(re.sub(r'^', 'Start-', 'line'))

#example 8
import re

print(re.findall(r'\d+', 'There are 3 cats and 4 dogs'))
print(re.findall(r'[A-Z]', 'Python Is Great'))
print(re.findall(r'colou?r', 'color and colour'))
print(re.findall(r'\b\w{4}\b', 'This text has four word size words'))
print(re.findall(r'\s', 'space here and there'))
print(re.findall(r'\w+', 'List all words here123'))
print(re.findall(r'[aeiou]', 'Count vowels in sentence'))

#example 9
import re

matches = re.finditer(r'\d+', 'Item 1 costs 20 and 30 more')
for m in matches:
    print(m.group())

matches = re.finditer(r'\w+', 'List all words here')
for m in matches:
    print(m.group())

matches = re.finditer(r'[A-Z]', 'Python Is Powerful')
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

matches = re.finditer(r'\d{2}', '12 34 56 78')
for m in matches:
    print(m.group())

# example 10
import re

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

#example 11
import re

print(re.findall(r'\d+', 'Find 123 and 456'))
print(re.findall(r'\D+', 'Only words and spaces 123'))
print(re.findall(r'\s+', 'Spaces are \t included \n here'))
print(re.findall(r'\S+', 'Non-space characters only'))
print(re.findall(r'\w+', 'Words_and123numbers'))
print(re.findall(r'\W+', '!!@@##$$ symbols only'))
print(re.findall(r'^Hello', 'Hello there!'))


# more examples regular expression


# example 6
import re
text = "My number is 98765"
match = re.search(r"\d+", text)
if match:
    print("Number found:", match.group())
# example 7
import re
text = "Python is fun"
words = re.findall(r"\w+", text)
print("Words:", words)

# example 8
import re
text = "apple, banana mango orange"
items = re.split(r"[,\s]+", text)
print(items)
# ex 8
import re
text = "Python is awesome"
new_text = re.sub(r"\s", "-", text)
print(new_text)
#  ex 9
import re
phone = "9876543210"
if re.fullmatch(r"[6-9]\d{9}", phone):
    print("Valid phone number")
else:
    print("Invalid number")
# 10
import re
text = "NASA and ISRO are space agencies."
caps = re.findall(r"\b[A-Z]{2,}\b", text)
print("Capital words:", caps)
# 11
import re
text = "apple123"
match = re.search(r"\w+(?=\d+)", text)  # matches 'apple' before digits
print(match.group())
# 12
import re

pan = "ABCDE1234F"
if re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", pan):
    print("Valid PAN")
else:
    print("Invalid PAN")

# 13
import re
text = "I have  4 dogs,  2 cats, and  5 parrot."
numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)

# 14 
import re

text = "Emails: john@gmail.com, raj@yahoo.com"
domains = re.findall(r"@(\w+)\.com", text)
print("Domains:", domains)

# 15
import re

print(re.fullmatch(r'\d+', '12345'))
print(re.fullmatch(r'\w+', 'Python3'))
print(re.fullmatch(r'abc', 'abc'))
print(re.fullmatch(r'[a-z]+', 'hello'))
print(re.fullmatch(r'[A-Z][a-z]+', 'Python'))
print(re.fullmatch(r'.+', 'JustText'))
print(re.fullmatch(r'colou?r', 'color'))

#16
import re
pattern = re.escape('[a-z]+')
print(re.match(pattern, '[a-z]+'))

#

