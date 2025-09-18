# Write a function that accepts a list and returns a new list with only unique elements.
def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 5, 1]
print("Original list:", numbers)
print("Unique elements:", unique_elements(numbers))
