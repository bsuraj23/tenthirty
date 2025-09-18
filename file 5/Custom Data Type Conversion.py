#Custom Data Type Conversion
#Write a function that takes a list of mixed data types (int, float, str, bool) and returns a dictionary with the count of each type.
def count_types(lst):
    counts={"int":0,"float":0,"str":0,"bool":0}
    for x in lst:
        if isinstance(x,bool): counts["bool"]+=1
        elif isinstance(x,int): counts["int"]+=1
        elif isinstance(x,float): counts["float"]+=1
        elif isinstance(x,str): counts["str"]+=1
    return counts

print(count_types([1,2.5,"hi",True,False,3]))
#Dynamic Input Parser: Implement a function that reads a line of input and parses it into appropriate Python data types (int, float, bool, str) based on its content.
def parse_value(s):
    s=s.strip()
    if s.lower() in ("true","false"): return s.lower()=="true"
    try: return int(s)
    except: pass
    try: return float(s)
    except: pass
    return s

print(parse_value("123"))   
print(parse_value("3.14"))  
print(parse_value("True"))  
print(parse_value("hello"))
# String Manipulation Suite: Given a string, write functions to:
def remove_vowels(s):
    return "".join(c for c in s if c.lower() not in "aeiou")

def char_freq(s):
    f={}
    for c in s:f[c]=f.get(c,0)+1
    return f

def substrings_k(s,k):
    return [s[i:i+k] for i in range(len(s)-k+1)]

print(remove_vowels("banana"))           
print(char_freq("banana"))               
print(substrings_k("banana",3))
#Remove all vowels Count the frequency of each character Return all substrings of length k Custom Array Operations: Implement a class that mimics Python’s list but only allows integers. Add methods for append, remove, pop, and slicing.
class IntList:
    def __init__(self): self.data=[]
    def append(self,x):
        if type(x)!=int: raise TypeError("ints only")
        self.data.append(x)
    def remove(self,x): self.data.remove(x)
    def pop(self,i=-1): return self.data.pop(i)
    def __getitem__(self,i): return self.data[i]

L=IntList()
L.append(1);L.append(2)
print(L.data) 
#Type Conversion Utility: Write a function that takes a dictionary with string values and converts them to their most likely Python types (int, float, bool, str).
def convert_dict(d):
    return {k:parse_value(v) for k,v in d.items()}

print(convert_dict({"a":"123","b":"3.5","c":"true"}))
#Prime Number Generator: Write a generator function that yields all prime numbers up to n using nested loops and control statements.
def primes(n):
    for num in range(2,n+1):
        for d in range(2,int(num**0.5)+1):
            if num%d==0: break
        else: yield num

print(list(primes(20)))
#Custom List Class with Advanced Features: Implement a class that supports list operations (append, insert, remove, pop, reverse, sort) and also supports undo/redo of operations.
def set_ops(a,b):
    return set(a)|set(b), set(a)&set(b), set(a)-set(b)

print(set_ops([1,2,3,4],[3,4,5]))