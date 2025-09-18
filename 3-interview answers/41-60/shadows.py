def compute_sum(numbers):
    sum_val = sum(numbers)  # avoid using 'sum' as a variable name
    return sum_val

numbers = [1, 2, 3, 4]
print("Sum of numbers:", compute_sum(numbers))
