#count datatypes
def cout_data_types(data_list):
    type_count ={"int": 0, "float":0, "str":0, "bool":0}

    for item in data_list:
        if isinstance(item, bool):
            type_count["bool"] += 1
        elif isinstance(item, int):
            type_count["int"] += 1
        elif isinstance(item, float):
            type_count["float"] += 1
        elif isinstance(item,str):
            type_count["str"] += 1
    return type_count

my_list = [10, 3.2,"hello", True]
result = cout_data_types(my_list)
print(result)


#Sring manupulation
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result = result + ch   
    return result

def char_frequency(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1
    return freq

def substrings_of_length_k(text, k):
    result = []
    for i in range(len(text) - k + 1):
        result.append(text[i:i+k])
    return result

s = "hello world"
print("Remove Vowels:", remove_vowels(s))
print("Char Frequency:", char_frequency(s))
print("Substrings of length 3:", substrings_of_length_k(s, 3))

# To a generator function that yields all prime numbers up to n using nested loops and control statements.
def prime_generator(n):
    for num in range(2, n + 1):        
        is_prime = True               
        for i in range(2, num):        
            if num % i == 0:          
                is_prime = False
                break                  
        if is_prime:
            yield num                  

n = 20
print(f"Prime numbers up to {n}:")
for prime in prime_generator(n):
    print(prime, end=" ")



# Custom list class with advanced features
class CustomList:
    def __init__(self):
        self.data = []         
        self.history = []       
        self.redo_stack = []    

    def _save_state(self):
        self.history.append(self.data.copy()) 

    def append(self, value):
        self._save_state()
        self.data.append(value)
        self.redo_stack.clear()

    def insert(self, index, value):
        self._save_state()
        self.data.insert(index, value)
        self.redo_stack.clear()

    def remove(self, value):
        self._save_state()
        self.data.remove(value)
        self.redo_stack.clear()

    def pop(self, index=-1):
        self._save_state()
        removed = self.data.pop(index)
        self.redo_stack.clear()
        return removed

    def reverse(self):
        self._save_state()
        self.data.reverse()
        self.redo_stack.clear()

    def sort(self):
        self._save_state()
        self.data.sort()
        self.redo_stack.clear()

    def undo(self):
        if self.history:
            self.redo_stack.append(self.data.copy()) 
            self.data = self.history.pop()
        else:
            print("Nothing to undo.")

    def redo(self):
        if self.redo_stack:
            self.history.append(self.data.copy())
            self.data = self.redo_stack.pop()
        else:
            print("Nothing to redo.")

    def show(self):
        return self.data

clist = CustomList()

clist.append(5)
clist.append(10)
clist.append(3)
print("After append:", clist.show())

clist.sort()
print("After sort:", clist.show())

clist.undo()
print("After undo:", clist.show())

clist.redo()
print("After redo:", clist.show())

clist.reverse()
print("After reverse:", clist.show())

clist.undo()
print("After undo:", clist.show())

#a function that takes two lists and returns their union, intersection, and difference using set operations.
def list_operations(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    union = set1 | set2           
    intersection = set1 & set2    
    difference = set1 - set2      

    return union, intersection, difference

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]

u, i, d = list_operations(a, b)

print("Union:", u)
print("Intersection:", i)
print("Difference (A - B):", d)

#List comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#even numbers
even_numbers = [n for n in numbers if n % 2 == 0]
#Square all odd numbers
squared_odds = [n ** 2 for n in numbers if n % 2 != 0]
#Create a list of tuples (number, square) for numbers divisible by 3
div_by_3_tuples = [(n, n ** 2) for n in numbers if n % 3 == 0]
print("Even Numbers:", even_numbers)
print("Squared Odd Numbers:", squared_odds)
print("Tuples (n, n^2) where n % 3 == 0:", div_by_3_tuples)


#implement custom functions
def my_max(lst):
    if not lst:
        return None  
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

def my_min(lst):
    if not lst:
        return None 
    minimum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum

def my_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

numbers = [5, 2, 8, 1, 9, 3]
print("List:", numbers)
print("My Max:", my_max(numbers))
print("My Min:", my_min(numbers))
print("My Sum:", my_sum(numbers))





