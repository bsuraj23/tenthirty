#Expert level Tricky & Practical
#81.Implement your own context manager without using with
class MyContext:
    def __enter__(self):
        print("Entered")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exited")

ctx = MyContext()
ctx.__enter__()
print("Doing work")
ctx.__exit__(None, None, None)
#82.Decorator class with parameters
class repeat:
    def __init__(self, times):
        self.times = times
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                func(*args, **kwargs)
        return wrapper

@repeat(3)
def hello():
    print("Hi!")

hello()
#84.Operator overloading
class Vector:
    def __init__(self,x,y):
        self.x=x;self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __repr__(self):
        return f"Vector({self.x},{self.y})"

v1=Vector(1,2); v2=Vector(3,4)
print(v1+v2)
#85.Lazy evaluation
def lazy_range(n):
    for i in range(n):
        yield i  

for x in lazy_range(5):
    print(x)

class LazyValue:
    def __init__(self, func):
        self.func = func
        self._value = None
    @property
    def value(self):
        if self._value is None:
            self._value = self.func()
        return self._value
#90.Implement your own event loop
import time
tasks = []

def call_later(delay, func):
    run_at=time.time()+delay
    tasks.append((run_at,func))

def run_loop():
    while tasks:
        now=time.time()
        for t in tasks[:]:
            run_at,func=t
            if now>=run_at:
                func()
                tasks.remove(t)

# Example:
call_later(1, lambda: print("Hello after 1s"))
call_later(2, lambda: print("Hello after 2s"))
run_loop()
