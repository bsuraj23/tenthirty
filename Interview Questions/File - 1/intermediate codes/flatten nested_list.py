#list comprehension nestedlist
def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]
print(flatten([[1,2],[3,4]]))

#using generators nested
def flatten(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item
print(list(flatten([[1,2],[3,4]])))

#normal nested list
nested_list=[[1,2],[3,4]]
flat=[]
for sublist in nested_list:
    for item in sublist:
        flat.append(item)
print(flat)