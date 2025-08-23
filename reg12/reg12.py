 # Check if a string contains only letters

import re

text = "HelloWorld"
if re.fullmatch(r"[A-Za-z]+", text):
    print(" Only letters")
else:
    print(" Contains non-letter characters")

#Validate an Email Address

import re

email = "example123@gmail.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,3}$"

if re.fullmatch(pattern, email):
    print(" Valid Email")
else:
    print(" Invalid Email")

# Find All Numbers in a String

import re

text = "There are 2 cats and 4 dogs."
numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)

# Validate a PAN Number (e.g., ABCDE1234F)

import re

pan = "ABCDE1234F"
pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

if re.fullmatch(pattern, pan):
    print(" Valid PAN")
else:
    print(" Invalid PAN")

# Check if String Starts with a Specific Word

import re

text = "Python is powerful"
if re.match(r"Python", text):
    print(" Starts with 'Python'")
else:
    print(" Does not start with 'Python'")

# Replace All Digits with #

import re

text = "My number is 9876543210"
new_text = re.sub(r"\d", "#", text)
print("Updated text:", new_text)

# Split a Sentence by Spaces

import re

sentence = "Python is easy to learn"
words = re.split(r"\s+", sentence)
print("Words:", words)

# Find All Capital Letters

import re

text = "My Name Is Archana"
capitals = re.findall(r"[A-Z]", text)
print("Capital letters:", capitals)