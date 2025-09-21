# #list of mixed data types (int, float, str, bool) and returns a dictionary with the count of each type.
def count_data_types(data_list):
    type_count = {'int': 0, 'float': 0, 'str': 0, 'bool': 0}
    
    for item in data_list:
        if isinstance(item, int) and not isinstance(item, bool): 
            type_count['int'] += 1
        elif isinstance(item, float):
            type_count['float'] += 1
        elif isinstance(item, str):
            type_count['str'] += 1
        elif isinstance(item, bool):
            type_count['bool'] += 1
            
    return type_count
data = [1, 2.5, 'hello', True, 3, False, 'world', 4.0,2.245, 5, 'python', True]
result = count_data_types(data) 
print(result) 

# #Implement a function that reads a line of input and parses it into appropriate Python data types (int, float, bool, str) based on its content.
def parse_input(input_line):
    input_line = input_line.strip()
    
    if input_line.lower() in ['true', 'false']:
        return input_line.lower() == 'true'
    try:
        if '.' in input_line:
            return float(input_line)
        else:
            return int(input_line)
    except ValueError:
        return input_line
user_input = input("Enter a value: ")
parsed_value = parse_input(user_input)
print(f"Parsed value: {parsed_value} (Type: {type(parsed_value)})")

#Given a string, write functions to Remove all vowels
def remove_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in input_string if char not in vowels])
input_str = "saipavan"
result = remove_vowels(input_str)
print(result) 

#Given a string, write functions to Count the frequency of each character
def char_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
input_str = "saipavan"
result = char_frequency(input_str)
print(result)

#Given a string, write functions to Return all substrings of length k
def substrings_of_length_k(input_string, k):
    return [input_string[i:i+k] for i in range(len(input_string) - k + 1)]
input_str = "saipavan"
k = 2
result = substrings_of_length_k(input_str, k)
print(result)

#Implement a class that mimics Python’s list but only allows integers. Add methods for append, remove, pop, and slicing.
class IntList:
    def __init__(self, iterable=None):
        self._data = []
        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError("Only integers are allowed")
        self._data.append(value)

    def remove(self, value):
        if value not in self._data:
            raise ValueError(f"{value} not found in list")
        self._data.remove(value)

    def pop(self, index=-1):
        return self._data.pop(index)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return IntList(self._data[key])
        return self._data[key]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"IntList({self._data})"
# Example usage:
int_list = IntList([1, 2, 3])   
print(int_list)
int_list.append(4)  
print(int_list)
int_list.remove(2)
print(int_list)
popped_value = int_list.pop()
print(f"Popped value: {popped_value}")
print(int_list)
sliced_list = int_list[0:2]
print(f"Sliced list: {sliced_list}")
print(f"Length of list: {len(int_list)}")

#Write a function that takes a dictionary with string values and converts them to their most likely Python types (int, float, bool, str).
def convert_dict_values(input_dict):
    def convert_value(value):
        value = value.strip()
        if value.lower() in ['true', 'false']:
            return value.lower() == 'true'
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            return value

    return {key: convert_value(val) for key, val in input_dict.items()}
input_dict = {'name': 'saipavan', 'age': '20', 'height': '5.8', 'is_student': 'true', 'weight': '70.5', 'graduated': 'false'}
converted_dict = convert_dict_values(input_dict)
print(converted_dict)
print({k: type(v) for k, v in converted_dict.items()})

#Write a generator function that yields all prime numbers up to n using nested loops and control statements.
def generate_primes(n):
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
n = 100
primes = list(generate_primes(n))
print(primes)
print(f"Total primes up to {n}: {len(primes)}")

#Write a function that takes two lists and returns their union, intersection, and difference using set operations.
def list_operations(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    union = list(set1 | set2)
    intersection = list(set1 & set2)
    difference = list(set1 - set2)
    
    return {
        'union': union,
        'intersection': intersection,
        'difference': difference
    }
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = list_operations(list1, list2)
print(result)   

#Build a function that takes a list of values and a target type, and returns a new list with all values cast to the target type, handling exceptions gracefully.
def cast_to_type(value_list, target_type):
    casted_list = []
    for value in value_list:
        try:
            casted_value = target_type(value)
            casted_list.append(casted_value)
        except (ValueError, TypeError):
            casted_list.append(None)  # or handle the exception as needed
    return casted_list
values = ['1', '2.5', 'hello', 'True', '3', 'world', '4.0', '5']
target_type = float
result = cast_to_type(values, target_type)
print(result)

#Given a list of numbers, use list comprehensions to: Find all even numbers Square all odd numbers
def process_numbers(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    squared_odds = [num**2 for num in num_list if num % 2 != 0]
    return even_numbers, squared_odds
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,45,78,20,47]
evens, squared_odds = process_numbers(numbers)
print(f"Even numbers: {evens}")
print(f"Squared odd numbers: {squared_odds}")

#Create a list of tuples (number, square) for numbers divisible by 3
def tuples_divisible_by_3(num_list):
    return [(num, num**2) for num in num_list if num % 3 == 0]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20 , 21, 22, 24, 27, 30]
result = tuples_divisible_by_3(numbers)
print(result)

#Implement a function that takes a string and returns a set of unique characters, then removes all vowels from the set.
def unique_chars_no_vowels(input_string):
    vowels = 'aeiouAEIOU'
    unique_chars = set(input_string)
    return unique_chars - set(vowels)
input_str = "saipavan"
result = unique_chars_no_vowels(input_str)
print(result)

#Implement your own versions of max, min, and sum functions for lists without using the built-in ones
def custom_max(num_list):
    if not num_list:
        return None
    max_value = num_list[0]
    for num in num_list:
        if num > max_value:
            max_value = num
    return max_value    
def custom_min(num_list):
    if not num_list:
        return None
    min_value = num_list[0]
    for num in num_list:
        if num < min_value:
            min_value = num
    return min_value
def custom_sum(num_list):
    total = 0
    for num in num_list:
        total += num
    return total
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"Custom Max: {custom_max(numbers)}")
print(f"Custom Min: {custom_min(numbers)}")
print(f"Custom Sum: {custom_sum(numbers)}")




