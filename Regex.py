import re

# 1. Check if the string contains only digits
text1 = "12345"
if re.fullmatch(r"\d+", text1):
    print("Text1 contains only digits.")
else:
    print("Text1 contains non-digit characters.")

# 2. Extract email from a sentence
sentence = "Please contact us at support@example.com for help."
email_match = re.search(r"\b[\w.-]+@[\w.-]+\.\w+\b", sentence)
if email_match:
    print("Found email:", email_match.group())
else:
    print("No email found.")

# 3. Find all words that start with a capital letter
text2 = "My name is Sindhuja and I live in India."
capital_words = re.findall(r"\b[A-Z][a-z]*\b", text2)
print("Capitalized words:", capital_words)