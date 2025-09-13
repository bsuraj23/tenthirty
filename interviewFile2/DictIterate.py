my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in my_dict:
    print(key)
for value in my_dict.values():
    print(value)
    
for index ,(key,value) in enumerate(my_dict.items()):
    print(index,key,value)   