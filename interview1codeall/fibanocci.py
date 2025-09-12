class Fib:
    def __init__(self, n):
        self.n=n; self.a=0; self.b=1
    def __iter__(self): return self
    def __next__(self):
        if self.n<=0: raise StopIteration
        self.n-=1
        val=self.a
        self.a,self.b=self.b,self.a+self.b
        return val
for x in Fib(5):
    print(x)

#Decorator to log execution time
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        print("Time:",time.time()-start)
        return result
    return wrapper
@timer
def work():
    for i in range(1000000): pass
work()

#Generator for even numbers upto N
def even_gen(n):
    for i in range(0,n+1,2):
        yield i
print(list(even_gen(20)))

#Flatten in a nested list
nested=[[1,2],[3,4]]
flat=(x for sub in nested for x in sub)
print(flat)