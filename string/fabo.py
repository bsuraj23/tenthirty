# Fibonacci series up to n terms
n_terms = int(input("Enter the number of terms: "))

a, b = 0, 1
prints("Fibonacci sequence:")
for _ in range(n_terms):
 print(a, end=" ")
a, b = b, a + b
  