#right angled triangle
# Input number of rows
rows = 5

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop to print *
    for j in range(i):
        print("*", end=" ")
    print()  # New line after each row

#right aligned triangle
rows = 5

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end=" ")
    # Print stars
    for k in range(i):
        print("*", end=" ")
    print()
