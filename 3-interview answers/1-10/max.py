def my_max(iterable):
    if not iterable:  # handle empty list
        raise ValueError("my_max() arg is an empty sequence")
    
    maximum = iterable[0]   # assume first element is max
    for item in iterable[1:]:
        if item > maximum:
            maximum = item
    return maximum

# Example usage
print(my_max([3, 7, 2, 14, 5]))   # 9
print(my_max([-6, -37, -50]))    # -3
