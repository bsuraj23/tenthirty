def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):       # if item is a list, flatten it
            flat_list.extend(flatten(item))
        else:                            # otherwise, just add the item
            flat_list.append(item)
    return flat_list

# Example usage
nested = [[1, 2], [3, 4], [5, [6, 7]], 8]
print(flatten(nested))   # [1, 2, 3, 4, 5, 6, 7, 8]
