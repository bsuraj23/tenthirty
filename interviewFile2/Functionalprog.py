from functools import reduce

nums=[1,2,3,4]

print(list(map(lambda x: x**2, nums)))   # applies to all

print(list(filter(lambda x: x%2 == 0,nums)))  #stores if in condition

print(reduce(lambda x,y :  x+y, nums))  #single value

# when filter is useful
ages=[12,54,23,65,11,13,18]

adult= filter(lambda x: x>=18, ages)
print(list(adult))

#reduce 
nms=[1,2,3,4,5]
product= reduce(lambda x,y: x*y, nms)
print(product)

#lamda and list comprehension
dgt= [5,6,7,8]
squares1=[ n**2 for n in dgt]
print(squares1)

squares2=(list(map(lambda x : x**2, dgt )))
print(squares2)