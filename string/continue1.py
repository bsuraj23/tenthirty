# This program prints odd numbers from 1 to 10
i = 10
while i < 10:
    i += 1
    if i % 2 == 0:
        continue #Skip even numbers  
    print(i)