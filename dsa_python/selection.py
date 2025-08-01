# n=[1,3,2,5,4,6]
# for i in range(len(n)):
#     min=i
#     for j in range(i+1,len(n)):
#         if n[j] < n[min]:
#             min=j
#     #swap with minimum number
#     n[i],n[min]=n[min],n[i]

# print(n)
            
    
arr=[1,3,2,5,4]
n=len(arr)
for i in range(n):
    min=i
    for j in range(i+1,n):
        if arr[j] < arr[min]:
            min=j
    arr[i],arr[min]=arr[min],arr[i]

print(arr)