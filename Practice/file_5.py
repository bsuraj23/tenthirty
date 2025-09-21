#Custom Data Type Conversion
def count_data_types(data):
    type_count = {"int": 0, "float": 0, "str": 0, "bool": 0}
    for item in data:
        if isinstance(item, int) and not isinstance(item, bool):
            type_count["int"] += 1
        elif isinstance(item, float):
            type_count["float"] += 1
        elif isinstance(item, str):
            type_count["str"] += 1
        elif isinstance(item, bool):
            type_count["bool"] += 1
    return type_count


#Dynamic Input Parser
def dynamic_parser(input_str):
    values = input_str.split()
    parsed = []
    for val in values:
        if val.lower() in ["true", "false"]:
            parsed.append(val.lower() == "true")
        elif val.replace('.', '', 1).isdigit():
            parsed.append(float(val) if '.' in val else int(val))
        else:
            parsed.append(val)
    return parsed


#String Manipulation Suite
def remove_vowels(s):
    return ''.join(ch for ch in s if ch.lower() not in "aeiou")

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

def substrings_of_length_k(s, k):
    return [s[i:i+k] for i in range(len(s)-k+1)]


#Custom Array Operations
class IntList:
    def __init__(self):
        self.data = []

    def append(self, value):
        if isinstance(value, int):
            self.data.append(value)

    def remove(self, value):
        if value in self.data:
            self.data.remove(value)

    def pop(self, index=-1):
        return self.data.pop(index)

    def slice(self, start, end):
        return self.data[start:end]


#Type Conversion Utility
def convert_dict_values(d):
    result = {}
    for key, value in d.items():
        val = value.strip()
        if val.lower() in ["true", "false"]:
            result[key] = val.lower() == "true"
        elif val.replace('.', '', 1).isdigit():
            result[key] = float(val) if '.' in val else int(val)
        else:
            result[key] = val
    return result


#Prime Number Generator
def prime_generator(n):
    for num in range(2, n+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


#Custom List Class with Advanced Features
class AdvancedList:
    def __init__(self):
        self.data = []
        self.history = []
        self.redo_stack = []

    def _save_state(self):
        self.history.append(self.data[:])

    def append(self, value):
        self._save_state()
        self.data.append(value)

    def insert(self, index, value):
        self._save_state()
        self.data.insert(index, value)

    def remove(self, value):
        self._save_state()
        self.data.remove(value)

    def pop(self, index=-1):
        self._save_state()
        return self.data.pop(index)

    def reverse(self):
        self._save_state()
        self.data.reverse()

    def sort(self):
        self._save_state()
        self.data.sort()

    def undo(self):
        if self.history:
            self.redo_stack.append(self.data[:])
            self.data = self.history.pop()

    def redo(self):
        if self.redo_stack:
            self.history.append(self.data[:])
            self.data = self.redo_stack.pop()


#Set Operations
def set_operations(list1, list2):
    s1, s2 = set(list1), set(list2)
    return {"union": s1 | s2, "intersection": s1 & s2, "difference": s1 - s2}


#Type Casting Engine
def type_cast(values, target_type):
    result = []
    for v in values:
        try:
            result.append(target_type(v))
        except (ValueError, TypeError):
            result.append(None)
    return result


#List Comprehension Challenge
def list_comprehension_challenge(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    odd_squares = [n**2 for n in numbers if n % 2 != 0]
    div3_pairs = [(n, n**2) for n in numbers if n % 3 == 0]
    return evens, odd_squares, div3_pairs


#Set Membership and Manipulation
def unique_chars_no_vowels(s):
    chars = set(s)
    vowels = set("aeiouAEIOU")
    return chars - vowels


#Function Decorator for Logging
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


#Deep Copy vs Shallow Copy Demonstration
import copy
def demonstrate_copy():
    original = [[1, 2], [3, 4]]
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)
    original[0][0] = 99
    return {"original": original, "shallow": shallow, "deep": deep}


#Custom Implementation of max, min, sum
def custom_max(lst):
    max_val = lst[0]
    for x in lst[1:]:
        if x > max_val:
            max_val = x
    return max_val

def custom_min(lst):
    min_val = lst[0]
    for x in lst[1:]:
        if x < min_val:
            min_val = x
    return min_val

def custom_sum(lst):
    total = 0
    for x in lst:
        total += x
    return total


#Advanced Control Flow
def custom_filter(numbers):
    result = []
    for n in numbers:
        if n < 0:
            break
        if n % 3 == 0:
            continue
        result.append(n)
    return result
