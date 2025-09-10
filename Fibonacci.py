#Fibonacci program in Python

n = int(input("Enter number of terms: "))

#First two terms
a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to", n, "term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1