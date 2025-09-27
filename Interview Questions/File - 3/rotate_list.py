#Rotate a list by `k` elements (circular shift).

def rotate_list(lst,k):
    n=len(lst)
    k=k%n    #handle  k>n
    return lst[k:]+lst[:k]
lst=[1,2,3,4,5]
print(rotate_list(lst,3))    # [4,5,1,2,3]

