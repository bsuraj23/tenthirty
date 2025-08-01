n=[1,3,2,4,7,5]
if len(n) > 1:
    piv=n[0]
    left=[]
    right=[]
    
    #appending left and right sides
    for i in n[1:]:
        if i < piv:
            left.append(i)
        else:
            right.append(i)
            
    #Sorting left side
    for i in range(len(left)):
        for j in range(i+1,len(left)):
            if left[i] > left[j]:
                left[i],left[j]=left[j],left[i]
    
    #sorting right side
    for i in range(len(right)):
        for j in range(i+1,len(right)):
            if right[i] > right[j]:
                right[i],right[j]=right[j],right[i]
    
    sor=left+ [piv] +right
else:
    sor=n
print(sor)
            

            