#Expert-Level Tricky & Practical
# How do you implement your own context manager without using with?
# A context manager has two special methods:
# __enter__: called when entering the block
# __exit__: called when leaving (even if exceptions occur) -->
class FileManager:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

fm = FileManager("test.txt", "w")
f = fm.__enter__()     
f.write("Hello!")
fm.__exit__(None, None, None)  

#How do you implement your own decorator class with parameters?
class repeat:
    def __init__(self, times):
        self.times = times
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                func(*args, **kwargs)
        return wrapper
@repeat(3)
def say_hello():
    print("Hello")
say_hello()

#What is the difference between __new__ and __init__?
# __new__:
# Creates a new instance of the class.
# It’s a class method (first arg = cls).
# __init__:
# Initializes the instance (already created).
# It’s an instance method (first arg = self).
class Demo:
    def __new__(cls, *args):
        print("Creating instance")
        return super().__new__(cls)
    def __init__(self, x):
        print("Initializing with", x)
obj = Demo(42)

# How do you implement operator overloading in Python?
# You override magic methods like __add__, __sub__, __lt__, etc.
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
v1, v2 = Vector(2,2), Vector(3,4)
print(v1 + v2)   

# How do you implement lazy evaluation in Python?
# Lazy evaluation = delay computation until needed.
# Generators (built-in lazy evaluation):
def lazy_range(n):
    for i in range(n):
        yield i
nums = lazy_range(5)
print(next(nums)) 
class Lazy:
    def __init__(self, func):
        self.func = func
        self._value = None
        self._evaluated = False
    @property
    def value(self):
        if not self._evaluated:
            self._value = self.func()
            self._evaluated = True
        return self._value
obj = Lazy(lambda: sum(range(10**6)))
print(obj.value)  