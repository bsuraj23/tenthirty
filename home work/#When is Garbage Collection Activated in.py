#When is Garbage Collection Activated in Python?
#Garbage collection activates in two main ways:

# 1. Reference Count Reaches Zero (Immediate)
#Every object in Python has a reference count.When this count becomes zero, Python immediately deletes the object.

a = [1, 2, 3]
b = a
del a
del b  # Now no reference, list is deleted
# 2. Automatic Garbage Collector (for Cycles)
#Python also handles circular references (like when two objects reference each other).
#These are not caught by reference counting, so Python's garbage collector runs periodically to find and clean them.


# Python uses gc module internally

import gc

gc.collect()  # Force garbage collection manually

print(gc.get_threshold())  # Shows thresholds for triggering GC
print(gc.get_count())      # Shows current object count in generations
