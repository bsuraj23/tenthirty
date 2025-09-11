def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [5, 10, 2, 8, 99, 34]
print(find_largest(numbers))

