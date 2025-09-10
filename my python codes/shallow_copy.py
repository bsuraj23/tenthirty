import copy
original=[[1,2],[3,4]]
shallow_copy=copy.copy(original)
shallow_copy[1][1]=99
print(original)
print(shallow_copy)   #the original data also can change when you modify the reference object data