#Data Types & Variables
#1.Palindrome without slicing:
def is_palindrome(s):
    i,j=0,len(s)-1
    while i < j: 
        if s[i]!=s[j]: 
            return False
        i+=1
        j-=1
    return True
print(is_palindrome("madam"))
print(is_palindrome("hello"))
#2.Remove duplicates without set():
def remove_dupes(lst):
     result=[]
     for x in lst:
         if x not in result: result.append(x)
     return result
print(remove_dupes([1,2,2,3]))
#3.Merge two dicts:
def merge_dicts(d1,d2):
     merged=d1.copy(); 
     merged.update(d2); 
     return merged
print(merge_dicts({'a':1,'b':2},{'b':3, 'c':4}))
#4.Frequency of chars:
from collections import Counter
freq=Counter('hello')
print(freq)
#5.Custom max():
def my_max(iterable):
     m=None
     for x in iterable:
         if m is None or x>m: m=x
     return m
print(my_max([1,2,5,9]))