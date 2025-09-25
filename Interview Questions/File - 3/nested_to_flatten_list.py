#Write code to flatten a nested list (e.g. `[[1,2],[3,4]] → [1,2,3,4]`).

#method-1
nested=[[1,2],[3,4]]
flatten=[]
for list in nested:
    for flat in list:
        flatten.append(flat)
print(flatten)

#method-2 list comprehension
def flatten(nested):
    return [flat for sublist in nested for flat in sublist]
print(flatten(nested))

