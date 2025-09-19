#Data structures & Algorithms in python
#41.Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if node is None:
                return False
        return node.is_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return False
        return True

# Example
t = Trie()
t.insert("apple")
print(t.search("apple"))   
print(t.search("app"))     
print(t.starts_with("app"))
#42.Thread safe queue
from queue import Queue
q = Queue()

q.put(10)
q.put(20)
print(q.get()) 
print(q.get())
#43.Custom linked list class with insert,delete and search
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new

    def search(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False

    def delete(self, val):
        prev, cur = None, self.head
        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return
            prev, cur = cur, cur.next

    def show(self):
        cur, res = self.head, []
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)

ll = LinkedList()
ll.insert(3); ll.insert(2); ll.insert(1)
ll.show()           
ll.delete(2)
ll.show()          
print(ll.search(3))
#44.Priority queue in python
import heapq
pq = []
heapq.heappush(pq, (1,"urgent"))
heapq.heappush(pq, (5,"low"))
print(heapq.heappop(pq))
#45.Sorting large datasets
big_list = [5,1,9,3]
print(sorted(big_list))
#46.Balanced binary search tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if not root: return False
    if key == root.key: return True
    if key < root.key: return search(root.left, key)
    return search(root.right, key)

root = None
for k in [10,5,15]:
    root = insert(root,k)
print(search(root,15))
#47.Graph traversal
graph = {
  'A': ['B','C'],
  'B': ['D'],
  'C': ['E'],
  'D': [],
  'E': []
}

def bfs(start):
    visited, queue = set(), [start]
    order = []
    while queue:
        u = queue.pop(0)
        if u not in visited:
            visited.add(u)
            order.append(u)
            queue.extend(graph[u])
    return order

def dfs(start, visited=None):
    if visited is None: visited=set()
    visited.add(start)
    order = [start]
    for v in graph[start]:
        if v not in visited:
            order += dfs(v,visited)
    return order

print(bfs('A'))  
print(dfs('A'))
#48.Detect cycles in a directed graph
def has_cycle(graph):
    visited=set()
    stack=set()

    def dfs(node):
        visited.add(node)
        stack.add(node)
        for v in graph[node]:
            if v not in visited:
                if dfs(v): return True
            elif v in stack:
                return True
        stack.remove(node)
        return False

    for n in graph:
        if n not in visited:
            if dfs(n): return True
    return False

g={'A':['B'],'B':['C'],'C':['A']}
print(has_cycle(g))
#49.Rate limiter
import time

class RateLimiter:
    def __init__(self, limit, interval):
        self.limit=limit
        self.interval=interval
        self.calls=[]

    def allow(self):
        now=time.time()
        self.calls=[c for c in self.calls if now-c<self.interval]
        if len(self.calls)<self.limit:
            self.calls.append(now)
            return True
        return False

rl=RateLimiter(5,10)
print(rl.allow()) 
#50.Distributed counter
counter=0

def increment():
    global counter
    counter+=1

increment()
increment()
print(counter)