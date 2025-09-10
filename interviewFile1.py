#reverse string
string="soham"
rev=""
for ch in string:
    rev= ch+rev
print(rev)    

#largest in list
lst=[1,2,3,4,5]
largest=lst[0]

for i in lst:
    if i> largest:
        largest=i
print(largest)         

#count vowels
str= "SohamRaibole"
vowels="AEIOUaeiou"
count=0

for ch in str:
    if ch in vowels:
        count+=1
print(count)          

#prime no
n = 7
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print("false")
else :
    print("true")        
    
 #fibonacci
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+ fibonacci(n-2)
print(fibonacci(10))    

#decorator
def decorator(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper

@decorator
def greet():
    print("hello world")


greet()

#even number
def even(num):
    for i in range(0,num+1,2):
        yield i
        
for num in even(10):
    print(num, end=" ")    
    
print()      
    
#flatten a sublist
sblst=[[1,2],[3,4],[5,6]]
flat=[]

for lt in sblst:
    for item in lt:
        flat.append(item)
print (flat)    

#map and filter

nums= [1,2,3,4,5,6,7,8]

even = filter (lambda x:  x%2==0, nums)

sqr= map (lambda x : x**2, even)

print(list(sqr))