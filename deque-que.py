1. deque (from collections module)

from collections import deque

Full name: Double-Ended Queue

Can add/remove from both ends efficiently (append, appendleft, pop, popleft)
Faster than queue.Queue for most pure Python queue operations
Thread-safe only for individual operations (not suitable for complex multithreading)
Ideal for simple FIFO/LIFO queues or sliding window problems



program:

from collections import deque

dq = deque()
dq.append('a')       # Add to right
dq.appendleft('b')   # Add to left
print(dq.pop())      # Remove from right → 'a'
print(dq.popleft())  # Remove from left → 'b'

🔸 2. queue.Queue (from queue module)


from queue import Queue

Thread-safe queue with locking mechanisms
Supports blocking operations (put(), get(), etc)
Slower than deque for single-threaded usage
Ideal for multithreaded programs (e.g., producer-consumer)


program:
from queue import Queue

q = Queue()
q.put(1)             # Enqueue
q.put(2)
print(q.get())       # Dequeue → 1
print(q.get())       # Dequeue → 2

comparision:

Feature      	                deque (collections)	                                         Queue (queue)
Supports both ends              ✅ (appendleft, popleft)	                                      ❌
Thread-safe    	                Partially (single ops)                                    	    ✅ (fully, with locks)
Speed (single-thread)	        ✅ Faster	                                                   ❌ Slower
Blocking operations	            ❌	                                                           ✅ (put(), get())
Suitable for multithreading 	❌ Basic only	                                               ✅ Best choice
LIFO support	                ✅ (pop)	                                                       ❌ (use LifoQueue instead)

