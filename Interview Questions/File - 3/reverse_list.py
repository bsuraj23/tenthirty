# Reverse a list **in place** without using `[::-1]` or `reverse()`.

def reverse_list(lst):
    left,right=0,len(lst)-1
    while left<right:
        lst[left],lst[right]=lst[right],lst[left]
        left+=1
        right-=1
    return lst

lst=[5,6,7,8,1,2,3,4]
print(reverse_list(lst))