import re

# Sample text containing emails
text = "Contact us at swathiteju08@gmail.com or tejupandu@mail.org. You can also reach admin123@domain.co.in"

# Regular expression pattern for emails
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

# Find all matching emails
emails = re.findall(pattern, text)

# Output the result
print("Extracted Emails:", emails)
