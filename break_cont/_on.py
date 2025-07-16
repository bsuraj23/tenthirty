# for i in range(1, 6):
#     if i % 2 == 0:
#         continue
#     print("Odd number:", i)

for i in range(1, 10):
    for j in range(1, i + 1):
        if (i+j) ==10:
            continue
        print("Skipping when sum is 10 and sum is:", i + j)