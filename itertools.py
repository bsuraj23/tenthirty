import itertools

count = 0
for i in itertools.cycle('AB'):
    if count > 7:
        break
    print(i, end=" ")
    count += 1