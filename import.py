#itertools
import itertools
items = ['A', 'B', 'C','D']
comb = list(itertools.combinations(items, 3))
print("combination of 3 elements:", comb)

#datetime
import datetime
now = datetime.datetime.now()
print("current date and time:", now)

#strftime
import datetime

# Get current date and time
now = datetime.datetime.now()


#Format using strftime
import datetime
now = datetime.datetime.now()
print("Default datetime:", now)
print("Year-Month-Day:", now.strftime("%Y-%m-%d"))
print("Day/Month/Year:", now.strftime("%d/%m/%Y"))
print("Full date and time:", now.strftime("%A, %B %d, %Y %I:%M %p"))
print("24-hour time:", now.strftime("%H:%M:%S"))
print("Weekday name:", now.strftime("%A"))
print("Month name:", now.strftime("%B"))


#calender
import calendar
year = 2025
month = 7
print("calendar of the july 2025:")
print(calendar.month(year,month))

print("full calendar for 2025:")
print(calendar.calendar(year))


#ramdom
import random
print("Random float (0 to 1):",random.random())
print("Random integer(1 to 100):",random.randint(1,100))     #returns integer between 1 to 100
fruits = ['apple','banana','mango']
print("Random fruits:",random.choice(fruits))
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print("Random numbers:",numbers)


#pop
fruits = ['mango','apple','banana','cherry']
removed_item = fruits.pop(1)
print("removed item:",removed_item)
print("update list:",fruits)

fruits = []

# Adding elements using append()
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
print("List after adding:", fruits)

# Removing last element using pop()
removed = fruits.pop()
print("Popped item:", removed)
print("List after popping:", fruits)


#queue
queue = []

# Enqueue: Adding elements at the end
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue after enqueue:", queue)

# Dequeue: Removing elements from the front
first_item = queue.pop(0)
print("Dequeued item:", first_item)
print("Queue after dequeue:", queue)
