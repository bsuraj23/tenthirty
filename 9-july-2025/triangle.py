
#write a code for printing a star without using the logic which is used in class
rows = 15
for i in range(1, rows + 1):
    stars = '*' * (2 * i - 1)
    print(stars.center(2 * rows - 1))