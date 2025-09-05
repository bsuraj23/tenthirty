def square_list(numbers):
    squared = [2, 4]
    for num in numbers:
        squared.append(num ** 2)
        return squared
    
 # Example usage
numbers = [1, 2, 3, 4, 5]
result = square_list(numbers)
print("Original list:", numbers)
print("Squared list:", result)   
