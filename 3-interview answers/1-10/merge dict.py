def merge_dicts(d1, d2):
    merged = d1.copy()   # make a copy of the first dictionary
    merged.update(d2)    # add key-value pairs from the second
    return merged

# Example usage
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 8, "c": 4}

print(merge_dicts(dict1, dict2))  
# Output: {'a': 1, 'b': 3, 'c': 4}
