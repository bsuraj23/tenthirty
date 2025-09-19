#Python Basics

1. Python’s key features – Easy to read, free, cross-platform, large libraries, object-oriented, supports multiple paradigms.

2. Interpreted language – Code runs line by line by the Python interpreter, no need to compile separately.

3. Wrong indentation – Python uses indentation to mark code blocks. Wrong indentation gives an Indentation Error.

4. Keywords – Reserved words like if, for, while. They have special meaning and cannot be used as variable names.

5. Python 2 vs 3 – Python 3 is newer; print is a function; better Unicode support; integer division differs; Python 2 is outdated.

#Data Types & Variables

6. Mutable vs Immutable – Mutable can change (list, dict, set). Immutable cannot change (int, float, str, tuple).

7. list / tuple / set / dict

list: ordered, changeable.

tuple: ordered, cannot change.

set: unordered, unique items.

dict: key–value pairs.

8. Built-in types – Numbers, strings, lists, tuples, sets, dicts, booleans, None.

9. is vs == – == checks values; is checks if two names point to the same object.

10. Integers and floats in memory – Stored as objects. Integers are arbitrary precision; floats follow IEEE-754 double precision.

#Lists, Strings & Collections

11. append() vs extend() – append() adds one item; extend() adds items from another iterable.

12. Shallow vs Deep copy – Shallow copy copies only top level (shared inner objects). Deep copy copies everything recursively.

13. Remove duplicates – Use list(set(mylist)) or loop and check manually.

14. Slicing – seq[start:stop:step] makes a new sequence with that range. Works on lists and strings.

15. Reverse a string – s[::-1].

#Control Flow & Loops

16. break / continue / pass –

break: exit loop.

continue: skip to next iteration.

pass: do nothing (placeholder).

17. else in loops – Runs only if the loop ends normally (no break).

18. enumerate() – Gives index and value while looping: for i,v in enumerate(lst).

19. Iterate dictionary –

for k,v in mydict.items():
    print(k, v)


20. List comprehension – Short way to create lists: [x*x for x in range(5)].

#Functions

21. Default arguments – Values given in function definition used when caller doesn’t pass them.

22. *args / kwargs – *args collects extra positional args as a tuple; **kwargs collects extra keyword args as a dict.

23. Pass-by-value vs reference – In Python everything is by object reference. Mutable objects can change inside a function.

24. Functions as variables – Yes, you can assign a function to a variable and call it later.

25. Lambda functions – Small anonymous functions: lambda x: x*x.

#OOP in Python

26. Classes and objects – Class = blueprint. Object = instance of the class.

27. Instance / Class / Static methods –

Instance: normal, gets self.

Class: gets cls, declared with @classmethod.

Static: no self or cls, declared with @staticmethod.

28. Dunder methods – Special names like __init__, __str__, __len__ used by Python internally.

29. __init__ – Constructor called when creating a new object to initialize it.

30. Polymorphism – Same method name can work on different object types.

#Iterators, Generators & Comprehensions

31. Iterable vs Iterator – Iterable can return an iterator (for loops over it). Iterator is the actual object that produces values one by one.

32. iter() / next() – iter() turns iterable into an iterator; next() gets the next item.

33. Generators – Functions that yield values lazily instead of returning all at once.

34. yield – Used in a generator to produce a value and pause the function.

35. Dict comprehensions – {k:v for k,v in pairs} makes a new dictionary.

#Exception Handling

36. Exception vs BaseException – BaseException is the top of all exceptions; Exception is for normal errors (KeyboardInterrupt etc. inherit directly from BaseException).

37. try / except / finally / else –

try: code that may error.

except: runs on error.

else: runs if no error.

finally: always runs.

38. Custom exceptions – Create a new class inheriting from Exception.

39. One except for many – Yes, use a tuple:

except (ValueError, TypeError):


40. No matching except – Program stops and shows the traceback.

#Decorators & Context Managers

41. Decorators – Functions that wrap other functions to add behavior.

42. Function returning function – Yes, Python supports this.

43. Higher-order function – Function that takes or returns other functions.

44. Context manager – Object that defines __enter__ and __exit__. Example: with open() as f:.

45. with vs try-finally – with automatically calls cleanup code; it’s a neater form of try-finally.

#Modules & Imports

46. Module vs Package – Module is one .py file. Package is a folder of modules with __init__.py.

47. __name__ == "__main__" – Code block that runs only if the file is run directly, not imported.

48. import vs from-import – import math then math.sqrt().
from math import sqrt lets you call sqrt() directly.

49. Relative imports – Use . or .. inside a package to import nearby modules.

50. Module search – Python looks in current dir, PYTHONPATH, installed site-packages.

#Namespaces & Scope

51. LEGB rule – Local → Enclosing → Global → Built-in order of name lookup.

52. Global vs Local – Global exists outside functions; local exists inside functions.

53. global keyword – Used inside a function to modify a global variable.

54. nonlocal keyword – Used inside nested functions to modify variable from outer function.

55. Same name in different scopes – Inner scope hides outer one.

#Data Handling

56. Read / write files –

with open('file.txt') as f: data=f.read()
with open('file.txt','w') as f: f.write('text')


57. Text vs Binary mode – 'r' or 'w' for text (strings). 'rb' or 'wb' for binary (bytes).

58. CSV files – Use csv module:

import csv
with open('f.csv') as f:
    for row in csv.reader(f): print(row)


59. JSON –

import json
js=json.dumps(obj)      # serialize
obj=json.loads(js)      # deserialize


60. Command-line arguments – Use sys.argv or argparse:

import sys
print(sys.argv[1])

#Functional Programming

61. map / filter / reduce –

map: apply function to each item.

filter: keep items that pass condition.

reduce: combine all items into one.

62. Lambda function – Small unnamed function: lambda x: x+1.

63. filter() example – Get even numbers:

list(filter(lambda x:x%2==0, [1,2,3,4]))


64. reduce() – Combine items cumulatively:

from functools import reduce
reduce(lambda a,b:a+b,[1,2,3]) # 6


65. List comprehension vs map() – List comprehension is often clearer and more flexible; map() just applies a function.