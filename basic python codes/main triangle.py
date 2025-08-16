rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

print("Another pattern")
for i in range(1,rows+1):
    print(" "*(rows-i)+(2*i-1)*"*")
