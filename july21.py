# ->               REGULAR EXPRESSIONS NOTES

#      What is Regex?
# Regular Expression (Regex) is a sequence of characters that defines a search pattern.

# ⦁	It’s used for:

# ⦁	Validating input (e.g., email, phone number)

# ⦁	Searching text

# ⦁	Extracting patterns

# ⦁	Replacing substrings


#         | Symbol | Meaning                               | Example Match              |
# | ------ | ------------------------------------- | -------------------------- |
# | `.`    | Any one character (except newline)    | `a.b` matches `acb`, `a9b` |
# | `\\d`   | A digit (`0-9`)                       | `\\d` matches `5` in `5kg`  |
# | `\\D`   | A non-digit                           | `\\D` matches `a` in `a7`   |
# | `\\w`   | Word character (letters, digits, `\_`) | `\\w` matches `A`, `3`, `\_` |
# | `\\W`   | Non-word character                    | `\\W` matches `@`, `#`, ` ` |
# | `\\s`   | Whitespace (space, tab, newline)      | `\\s` matches space         |
# | `\\S`   | Non-whitespace                        | `\\S` matches `a`, `3`, etc |
# | `^`    | Start of the string                   | `^A` matches `A` at start  |
# | `$`    | End of the string                     | `z$` matches `z` at end    |


# | Pattern           | What It Matches                            |
# | ----------------- | ------------------------------------------ |
# | `\\d{3}`           | Exactly 3 digits                           |
# | `\[A-Z]\[a-z]+`     | One uppercase + lowercase letters          |
# | `^\[a-zA-Z0-9\_]+$` | Entire string with only word chars         |
# | `\\d{2,4}`         | 2 to 4 digit numbers                       |
# | `^Hello`          | Only matches if string starts with "Hello" |
# | `abc$`            | Matches "abc" at end of string             |


# import re

# pattern = r'\d+'       # one or more digits
# text = "My age is 25."

# match = re.match(pattern, text)  # Match at start? ❌ No

# search = re.search(pattern, text)  # Anywhere? ✅ Yes
# print(search.group())  # Output: 25


# | You Want...     | Use This |
# | --------------- | -------- |
# | Any digit       | `\\d`     |
# | Any letter/word | `\\w`     |
# | Any space       | `\\s`     |
# | Repeat 1+ times | `+`      |
# | Specific set    | `\[a-z]`  |
# | Starts with     | `^text`  |
# | Ends with       | `text$`  |
# | Either A or B   | \`(A     | B)\\`


#                   Real-World Regex Patterns
# ✅ 1. Email Validation
# ^[\w.-]+@[\w.-]+\.\w+$
# Begins with word characters, dots or hyphens

# @ symbol in middle

# Ends with .com, .org, etc.

# ✔️ Matches: user.name123@example.com

# 2. Mobile Number (India format)

# ^[6-9]\d{9}$
# Starts with 6,7,8,9

# Followed by 9 digits

# ✔️ Matches: 9876543210
# ❌ Doesn't match: 1234567890

#                Useful Regex Functions in Python

# | Function       | Purpose                          |
# | -------------- | -------------------------------- |
# | `re.match()`   | Match only at the beginning      |
# | `re.search()`  | Search anywhere in the string    |
# | `re.findall()` | Return **all matches** as a list |
# | `re.sub()`     | Substitute (replace) parts       |