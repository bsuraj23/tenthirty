Advanced Internals & Performance
1. How Python manages memory internally
Python uses a private heap for all objects and data structures.
Memory management is handled by the Python Memory Manager.
It allocates memory in blocks and arenas (not directly from OS for each object).
Small objects (< 512 bytes) are allocated from pymalloc, which is faster.
Large objects are allocated using the system allocator (malloc).
Reference counting is the primary mechanism for memory deallocation.

2. Difference between id(), hash(), and is
id(obj) → returns a unique identifier (usually the memory address) of the object during its lifetime.
hash(obj) → returns an integer hash value (used in sets, dict keys). Objects must be hashable (immutable).
is → checks object identity (whether two variables point to the same object in memory).

3. How Python’s garbage collector works
Uses reference counting primarily.
If refcount(obj) reaches 0, the memory is freed.
To handle reference cycles (where objects reference each other), Python uses the cyclic garbage collector from the gc module, which detects unreachable objects.

4. Reference cycles and Python’s handling
A reference cycle occurs when objects reference each other, preventing their reference counts from ever reaching 0.
a = {}
b = {}
a["b"] = b
b["a"] = a  

5. Difference between deepcopy and pickle
deepcopy → creates a new copy of objects recursively in memory. It’s only for copying, not persistence.
pickle → serializes objects to a byte stream (can be saved to a file or sent over a network), and then deserializes back.

6. Shallow copy vs Deep copy vs Assignment
Assignment (=) → just copies the reference, not the object.
Shallow copy (copy.copy) → creates a new container, but references to the same inner objects.
Deep copy (copy.deepcopy) → creates a new container and recursively copies all nested objects.
Example:
import copy
lst = [[1, 2], [3, 4]]
a = lst            # assignment
b = copy.copy(lst) # shallow copy
c = copy.deepcopy(lst) # deep copy

7. How Python’s lists are implemented internally
Python lists are dynamic arrays.
Backed by a contiguous block of memory.
Over-allocated (extra space reserved) to allow efficient append().
Access = O(1), Append = Amortized O(1), Insert/Delete (middle) = O(n).

8. How Python implements dictionaries
Python dicts are implemented as hash tables with open addressing.
Each key’s hash determines its slot.
Collisions are resolved with probing (finding next available slot).
Resizing occurs when load factor is high (~2/3).
Since Python 3.6+, dicts also preserve insertion order.

9. Difference between OrderedDict and normal dict in Python 3.7+
Before Python 3.7: Only OrderedDict guaranteed insertion order.
From Python 3.7+: Regular dict also preserves insertion order (officially guaranteed in Python 3.7+).
OrderedDict extras:
Can reorder keys (move_to_end).
Equality check (==) respects order.

10. Profiling Python code
Use cProfile (built-in) → profiles function calls and execution time.
python -m cProfile myscript.py
Use timeit → for micro-benchmarking small code snippets.
Use line_profiler (pip install line-profiler) → for line-by-line timing.
Use memory_profiler (pip install memory-profiler) → to check memory usage.

 
Concurrency, Parallelism & Async
11. What is the Global Interpreter Lock (GIL)? Why does it exist?
GIL = a mutex in CPython ensuring only one thread executes Python bytecode at a time.
Exists because:
CPython’s memory management is not thread-safe.
Easier and faster to implement without fine-grained locks.
Downsides:
Prevents true parallel CPU-bound threads.
Still allows I/O-bound concurrency (because GIL is released during blocking I/O).

12. Multithreading vs Multiprocessing
Multithreading:
Multiple threads in one process.
Share memory space.
Limited by GIL (no parallel CPU-bound execution).
Best for I/O-bound tasks.
Multiprocessing:
Multiple independent processes, each with its own Python interpreter + memory.
No GIL restriction → true parallelism.
Best for CPU-bound tasks.

13. When to use threading vs multiprocessing
Use threading:
Network calls, file I/O, waiting on external events.
Example: web scraping, chat servers.
Use multiprocessing:
Heavy CPU tasks (e.g., image processing, ML computation).
Example: matrix multiplication, data processing.

14. What is asyncio in Python? How does it differ from threads?
asyncio = Python’s asynchronous I/O framework using event loop + coroutines.
Differences from threads:
Single-threaded concurrency (no GIL issues).
Cooperative multitasking → tasks yield control (await).
Threads = preemptive, asyncio = cooperative.
Lower memory overhead than threads.

15. Coroutines vs Generators
Generators:
Use yield.
Produce a sequence of values lazily.
Paused and resumed, but primarily for data generation.
Coroutines:
Use async def and await.
Can consume values, suspend execution, and resume.
Designed for concurrency (e.g., asyncio).

16. ThreadPoolExecutor vs ProcessPoolExecutor
ThreadPoolExecutor:
Uses threads.
Shares memory (but blocked by GIL for CPU-bound tasks).
Best for I/O-bound tasks.
ProcessPoolExecutor:
Uses multiple processes.
No GIL → true parallelism.
Higher overhead (IPC needed).
Best for CPU-bound tasks.

17. Cooperative vs Preemptive Multitasking
Cooperative multitasking:
Tasks voluntarily yield control (await).
Example: asyncio, coroutines.
More predictable, but a misbehaving task can block.
Preemptive multitasking:
OS scheduler forces context switches between tasks.
Example: threads, processes.
Safer, but more overhead (context switching).

18. Example: Async function fetching multiple URLs
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://python.org"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for i, r in enumerate(results):
            print(f"URL {i+1} length:", len(r))

asyncio.run(main())


19. Race conditions and Deadlocks
Race condition → outcome depends on unpredictable thread scheduling.
Example: two threads incrementing a shared counter without locks.
Fix: Use threading.Lock().
Deadlock → two threads wait forever on each other’s lock.
Example: Thread A holds Lock1 and waits for Lock2, Thread B holds Lock2 and waits for Lock1.
Fix: Consistent lock ordering, or use threading.RLock() / asyncio.Lock.

20. Inter-process communication (IPC) in Python
Python provides IPC mechanisms via multiprocessing:
Pipes → send data between processes.
Queues → thread/process-safe FIFO for communication.
Shared memory → multiprocessing.Value, multiprocessing.Array, or multiprocessing.shared_memory.
Managers → share higher-level objects (dict, list).


 Memory Optimization & Design
21. What are Python memory views?
memoryview = a built-in type that provides a view (window) into another object’s memory buffer without copying data.
Useful for large binary data processing (e.g., slicing bytes without making copies).
data = bytearray(b"Python")
mv = memoryview(data)
print(mv[0])      # 80 (ASCII 'P')
mv[0] = 120       # modifies original bytearray → 'xython'

22. Difference: bytes, bytearray, memoryview
bytes → immutable sequence of bytes.
bytearray → mutable version of bytes.
memoryview → lightweight object referencing the memory of bytes/bytearray (or any buffer-supporting object) without copying.

23. Reducing memory usage for large datasets
Use generators instead of lists (lazy evaluation).
Use array module (compact storage of numbers).
Use numpy arrays (efficient memory representation).
Use __slots__ to avoid per-object dict overhead.
Use iterators (itertools) instead of building full structures.
Use dataclasses with slots=True in Python 3.10+.
Process data in chunks (streaming).

24. Slots (__slots__) in Python classes
Normally, Python stores attributes in a dictionary (__dict__), which uses extra memory.
Defining __slots__ in a class tells Python to use a fixed set of attributes, removing __dict__.
 Saves memory (especially for millions of objects).

class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x, self.y = x, y
Trade-off: Cannot dynamically add new attributes.

25. Implementing an LRU Cache manually
Use an OrderedDict:
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # mark as recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # remove least recently used

26. How functools.lru_cache works internally
Implemented as a decorator wrapping a function.
Uses a dictionary for caching results.
Uses a linked list (ordered) to track usage (recent vs old).
Provides maxsize and cache_clear() options.
Evicts least recently used when cache is full.

27. Weak references (weakref)
Normal references increase an object’s reference count → prevents GC.
Weak references allow you to reference an object without increasing refcount.
Useful in caches, where you want objects to be garbage-collected if no strong refs remain.
import weakref
class A: pass
a = A()
r = weakref.ref(a)
print(r())  # access object
del a
print(r())  # None (collected)

28. Debugging a memory leak in Python
Tools:
gc module → gc.collect() and gc.garbage.
objgraph → visualize reference cycles.
tracemalloc → track memory allocations.
memory_profiler → line-by-line memory usage.
Common causes: reference cycles, global variables, large caches.
Solution: use weakrefs, context managers, manual cleanup.

29. Generators vs Lists for memory efficiency
Lists:
Store all elements in memory.
Random access (O(1)).
Bad for very large sequences.
Generators:
Lazy → compute one item at a time.
Uses constant memory regardless of size.
No random access, only sequential iteration.

30. Handling huge data (GBs) efficiently in Python
Use iterators and generators (yield).
Process data in chunks instead of loading everything into memory.
Use memory-mapped files (mmap) for huge binary/text files.
Use Pandas with chunksize for large CSVs.
Use Dask / Vaex for out-of-core processing.
Use multiprocessing for parallel chunks.
For numeric data → NumPy memmap (disk-backed arrays).

 Advanced OOP & Design Patterns
31. What are metaclasses in Python?
A metaclass is the "class of a class".
Just like classes create objects, metaclasses create classes.
Default metaclass = type.
Used for:
Enforcing coding rules.
Auto-registering classes.
Adding methods/properties automatically.

32. Difference between type() and class in Python
class → keyword for defining a class.
type():
If 1 arg → returns the type of an object.
If 3 args → dynamically creates a class.
# Using class
class A: pass
# Using type()
B = type("B", (object,), {"x": 42})

33. Singleton class in Python
Ensures only one instance exists.
Example:
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
Or use a decorator:
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper
@singleton
class MyClass: pass

34. Factory design pattern
Factory returns objects without exposing creation logic.
Example:
class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"
def animal_factory(kind):
    if kind == "dog": return Dog()
    if kind == "cat": return Cat()
    raise ValueError("Unknown animal")

35. Monkey patching
Modifying classes or modules at runtime.
Example:
class A:
    def greet(self): return "Hello"
def new_greet(self): return "Hi, patched!"
A.greet = new_greet
print(A().greet())  # "Hi, patched!"


36. Mixins in Python
Mixin = a class providing methods to be “mixed” into other classes, not meant to stand alone.
Promotes code reuse.
Example:
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
class Person(JSONMixin):
    def __init__(self, name): self.name = name

37. Duck typing
"If it looks like a duck and quacks like a duck, it’s a duck."
In Python → type doesn’t matter, behavior does.
Example:
def quack(obj):
    obj.quack()
class Duck:
    def quack(self): print("Quack!")
class Person:
    def quack(self): print("I can quack too!")

quack(Duck())    # Quack!
quack(Person())  # I can quack too!

38. Multiple inheritance & MRO
Python uses C3 linearization for MRO (Method Resolution Order).
Rule: Depth-first, left-to-right, but ensures consistent order.
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())
# [D, B, C, A, object]

39. Abstract Base Classes (abc module)
Used to define interfaces.
Cannot be instantiated unless abstract methods are implemented.
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self): pass

class Dog(Animal):
    def speak(self): return "Woof!"

40. Dependency injection in Python
Dependency Injection (DI) = passing dependencies into a class/function instead of hardcoding them.
Improves testability and flexibility.
Example:
class EmailService:
    def send(self, msg): print("Sending:", msg)
class Notification:
    def __init__(self, service):
        self.service = service
    def notify(self, msg):
        self.service.send(msg)
service = EmailService()
notif = Notification(service)  # Inject dependency
notif.notify("Hello!")



