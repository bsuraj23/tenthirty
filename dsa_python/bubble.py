n=[1,3,2,5,4,6]
for i in range(len(n)):
    for j in range(len(n)-1):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]
print(n)  # Output: [1, 2, 3, 4, 5, 6]