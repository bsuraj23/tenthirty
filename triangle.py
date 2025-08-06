rows = 5

for i in range(1, rows + 1):
    line = ''
    for j in range(rows - i):
        line += ' '
    for k in range(2* i - i):
        line +=  '*'
    print(line)