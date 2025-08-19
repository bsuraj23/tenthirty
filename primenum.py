for num in range(2, 51):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")

n = int(input("Enter a number: "))
for i in range (1,11):
 print(f"{n} x {i} = {n*i}")