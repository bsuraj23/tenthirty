#re.search()
import re

text = "My phone number is 9876543210"
pattern = r"\d{10}"  # pattern to match 10 digits

match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("Phone number not found.")

#re.findall()
    import re

text = "The prices are 45, 99, and 120 dollars"
pattern = r"\d+"

numbers = re.findall(pattern, text)
print("Numbers found:", numbers)

#re.sub()
import re

text = "User123 has score 456"
pattern = r"\d+"  # Match digits

new_text = re.sub(pattern, "#", text)
print("Updated text:", new_text)

