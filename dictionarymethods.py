#dict.keys
my_dict = {"a": 1, "b": 2}
print(my_dict.keys())
#dict values
print(my_dict.values())
#items 
print(my_dict.items())
#updated
my_dict.update({"c": 3})
print(my_dict)
#pop
value = my_dict.pop("b")
print(value)       
print(my_dict)
#clear
my_dict.clear()
print(my_dict)    
#dict copy
original = {"x": 10, "y": 20}
copy_dict = original.copy()
print(copy_dict)

   
