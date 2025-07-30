from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
from queue import PriorityQueue
import heapq

print("=== 1. Counter Example ===")
word = "banana"
counter = Counter(word)
print("Counter:", counter)

print("\n=== 2. namedtuple Example ===")
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Point: x = {p.x}, y = {p.y}")

print("\n=== 3. OrderedDict Example ===")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print("OrderedDict:", od)

print("\n=== 4. defaultdict Example ===")
dd = defaultdict(int)
dd['apple'] += 1
dd['banana'] += 2
print("defaultdict:", dd)

print("\n=== 5. deque Example ===")
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print("Deque after append:", dq)

print("\n=== 6. Most Common Character ===")
text = "programming"
char_counter = Counter(text)
most_common_char, count = char_counter.most_common(1)[0]
print(f"Most common character: '{most_common_char}' appears {count} times")

print("\n=== 7. Priority Queue using queue.PriorityQueue ===")
pq = PriorityQueue()
pq.put((2, "Low"))
pq.put((1, "Medium"))
pq.put((0, "High"))
print("PriorityQueue:")
while not pq.empty():
    priority, task = pq.get()
    print(f"Priority {priority} -> {task}")

print("\n=== 8. Priority Queue using heapq ===")
heap = []
heapq.heappush(heap, (3, "Low"))
heapq.heappush(heap, (1, "High"))
heapq.heappush(heap, (2, "Medium"))
print("heapq PriorityQueue:")
while heap:
    priority, task = heapq.heappop(heap)
    print(f"Priority {priority} -> {task}")

print("\n=== 9. Clear and Delete Queue ===")
queue = deque(["apple", "banana", "cherry"])
print("Original queue:", queue)
queue.clear()
print("Queue after clearing:", queue)
del queue
print("Queue deleted successfully (not printed to avoid error)")
