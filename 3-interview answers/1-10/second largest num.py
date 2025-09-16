def rotate_list(lst, k):
    n = len(lst)
    if n == 0:
        return lst
    
    k = k % n  # handle rotations larger than list length
    
    return lst[-k:] + lst[:-k]

# Example usage
nums = [1, 2, 3, 4, 5]
print(rotate_list(nums, 2))   # [4, 5, 1, 2, 3]
print(rotate_list(nums, -2))  # [3, 4, 5, 1, 2]  (left rotation)
