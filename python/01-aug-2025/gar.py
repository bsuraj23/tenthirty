import gc 

a = [1,2,3,4]
a = None

gc.collect() 
#it collects the garbage automatically in python it doesn't require to write gc.collect 


print("garbage collection is done ")
