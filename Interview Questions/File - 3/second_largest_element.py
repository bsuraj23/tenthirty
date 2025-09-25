#Find the second largest number in a list.
def second_largest(lst):
    return list(dict.fromkeys(lst))
lst=[1,2,5,4,8,8,4,3,8,9,43,67,45]
second=sorted(lst,reverse=True)
print(second_largest(second[1:2]))

#this is my own code





   
    

