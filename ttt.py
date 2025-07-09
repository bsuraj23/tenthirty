
rows = 5
for temp in range(1, rows + 1):
    for temp1 in range(rows - temp):
        print(" ", end="")
    for temp2 in range(temp):
        print("*", end="")
    print()
