import gc
a = [1, 2, 3]
b = a
del a
del b  

gc.collect()  
print(gc.get_threshold())  
