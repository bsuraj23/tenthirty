#zip is used to combine two lists into a dictionary
names=['Mike', 'John', 'Sara', 'Anna']
ages=[25, 30, 22, 28]
d = dict(zip(names, ages))
print("Dictionary created using zip:")
print(d)
