def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        # swap elements
        lst[left], lst[right] = lst[right], lst[left]
        
        left += 1
        right -= 1

# Example usage
nums = [1, 2, 3, 4, 5]
reverse_list(nums)
print(nums)  # [5, 4, 3, 2, 1]
