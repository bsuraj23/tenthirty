num = int(input("Enter a number to print its table: "))

# Print multiplication table up to 10
print(f"Multiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")