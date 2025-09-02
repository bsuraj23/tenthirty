# Student details
student_name = "Rām Kumar"  # Name contains a special character ā

# Marks in 5 subjects
marks = [85, 90, 78, 92, 88]

# 1. Total marks using sum()
total = sum(marks)
print("Total Marks:", total)

# 2. Highest marks using max()
highest = max(marks)
print("Highest Marks:", highest)

# 3. Lowest marks using min()
lowest = min(marks)
print("Lowest Marks:", lowest)

# 4. Average marks
average = total / len(marks)
print("Average Marks:", average)

# 5. Convert total marks to binary using bin()
binary_total = bin(total)
print("Total Marks in Binary:", binary_total)

# 6. Print ascii-safe version of name using ascii()
safe_name = ascii(student_name)
print("ASCII Safe Name:", safe_name)

# 7. Find Unicode of first letter using ord()
first_letter = student_name[0]
unicode_val = ord(first_letter)
print("Unicode of first letter:", unicode_val)

# 8. Convert Unicode back to character using chr()
character = chr(unicode_val)
print("Character from Unicode:", character)
