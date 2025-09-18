#44.How do you implement a priority queue in Python?
import heapq

pq = []  # empty priority queue

# Insert elements (priority, value)
heapq.heappush(pq, (2, "low priority"))
heapq.heappush(pq, (1, "high priority"))
heapq.heappush(pq, (3, "very low priority"))

# Pop elements by priority
while pq:
    priority, value = heapq.heappop(pq)
    print(f"{value} (priority {priority})")
