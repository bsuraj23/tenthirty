import copy
original=[[1,2],[3,4]]
deep_copy=copy.deepcopy(original)
deep_copy[0][1]=100
print(original)
print(deep_copy)    #the original data cannot change when you modify reference object data
 