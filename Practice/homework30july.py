#to list all attributes, functions, classes, and variables in a module
import os
print(dir(os))

#py_compile module is used to compile a Python source file (.py) into bytecode (.pyc)
import py_compile
py_compile.compile("C:\\A MET\\Git\\tenthirty\\Practice\\example.py")

#to get the most common repeated character from the collection or arrays.
from collections import Counter
data = "bananaapple"
counter = Counter(data)
most_common = counter.most_common()
print("Character counts:", most_common)
max_count = most_common[0][1]
most_repeated = [char for char, count in most_common if count == max_count]
print("Most repeated character(s):", most_repeated)
