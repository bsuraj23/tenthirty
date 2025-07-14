fruits = ["apple", "banana", "cherry"]

# Print the whole list
print("All fruits:", fruits)

# Accessing individual items
print("First fruit:", fruits[0])

# Adding a new fruit
fruits.append("orange")
print("After adding orange:", fruits)

# Removing a fruit
fruits.remove("banana")
print("After removing banana:", fruits)

# Loop through the list
print("List of fruits:")
for fruit in fruits:
    print("-", fruit)