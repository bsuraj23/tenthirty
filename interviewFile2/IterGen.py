# iterator and next

lst=[1,2,3,4]
itr= iter(lst)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


#generator (yeild)
def num(n):
    while n>0:
      n-=1
      yield n
    
for num in num(10):
    print(num)    
    
    
# yield keyword
def countdown(n):
    for i in range (1,n+1):
        
        yield i**2
        
sr= countdown(5)
print(next(sr))   
print(next(sr))
print(next(sr))   