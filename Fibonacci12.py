# Fibonacci series up to n terms
n = int(input("Enter number of terms: "))
a, b = 0, 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Fibonacci series up to a maximum number
max_num = int(input("Enter maximum value: "))
a, b = 0, 1

print("Fibonacci Series:")
while a <= max_num:
    print(a, end=" ")
    a, b = b, a + b
#Fibonacci Series Using Recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n_terms = int(input("Enter number of terms: "))

print("Fibonacci Series:")
for i in range(n_terms):
    print(fibonacci(i), end=" ")

# Generate n Fibonacci numbers and store in a list
n = int(input("Enter number of terms: "))
fib = [0, 1]

for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

print("Fibonacci Series:")
print(fib[:n])
