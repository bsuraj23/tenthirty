def remove_duplicates(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  
