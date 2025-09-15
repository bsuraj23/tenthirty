# Function to flatten a nested list
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):   # If the item is a list, extend recursively
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)   # If not a list, just append
    return flat_list

# Example
nested = [1, [2, [3, 4], 5], [6, 7], 8]
print("Nested List:", nested)
print("Flattened List:", flatten(nested))
