# nested =[[1, 2,], [3, 4]]
# flat = [item for sublist in nested for item in sublist]
# print(flat)
# using recursion
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
print(list(flatten(nested)))
