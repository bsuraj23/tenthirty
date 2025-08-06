n=["man","abb","man","bba"]
# removing duplicates from a list without using built-in functions
unique_list=[]
for i in n:
    unique_list.append(i)
    count=0
    
    # count occurrences of each element
    for j in unique_list:
        if i == j:
            count += 1
            
    # if count is greater than 1, remove the element
    if count > 1:
        unique_list.remove(i)
print("List after removing duplicates:", unique_list)