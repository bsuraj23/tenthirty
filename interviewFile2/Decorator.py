def myname(func):
    def wrapper():
        print("hello")
        func()
        print("how are you")
    return wrapper   
@myname
def greet():
    print("soham")
greet()    

#function returning other function
def outer():
    def inner():
        return "i am inner "
    return inner

a= outer() #returns inner and then goes to inner 
print(a())       

#eg2
def power(n):
    def square(x):
        return x**n
    
    return square

t = power(3)
y= power(2)

print(t(3))
print(y(3))

# higher order function
def square(x): return x*x
nums=[1,2,3]

result = map(square,nums)
print(list(result))

with open("file.txt", "w") as f:
    f.write("Hello")
