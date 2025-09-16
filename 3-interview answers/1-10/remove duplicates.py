def remove_duplicates(nums):
    unique = []
    for n in nums:
        if n not in unique:   # check before adding
            unique.append(n)
    return unique

# Example usage
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
print(remove_duplicates(numbers))  # [1, 2, 3, 4, 5]
