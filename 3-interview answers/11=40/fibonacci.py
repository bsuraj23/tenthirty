def fibonacci(n):
    a, b = 0, 1   # first two numbers
    for i in range(n):
        print(a, end=" ")   # print current number
        a, b = b, a + b     # update values

# Example usage
n = int(input("Enter number of terms: "))
fibonacci(n)
