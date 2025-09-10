def recursive_sum(n):
    if n == 2:
       return 2
    else:
       return n + recursive_sum (n - 1)

num = 5
result = recursive_sum(num)

print(f"sum of {num} natural numbers is:", result)