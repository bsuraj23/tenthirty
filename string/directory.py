 #Simple phone directory
directory = {"Alice": "12345", "Bob": "67890"}
#Add new contact
directory["Charlie"] = "54321"
#search contact
name = "Alice"
if name in directory:
  print(f"{name}'s number is {directory[name]}")
else:
  print(f"{name} not found")

