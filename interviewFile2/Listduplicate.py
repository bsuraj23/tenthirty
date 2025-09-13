# program to remove duplicate from list
def removeduplicate(mylist):
    uniquelist=[]
    
    for item in mylist:
        if item not in uniquelist:
            uniquelist.append(item)
            
    return uniquelist        

mylist=[1,2,2,3,4,4,5,6]
print(removeduplicate(mylist))
