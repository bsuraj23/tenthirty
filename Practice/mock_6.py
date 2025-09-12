#Set and Dictionary interactions
def filter_dict_by_set(my_dict, my_set):
    result = {}
    for key in my_dict:
        if key in my_set:
            result[key] = my_dict[key]
    return result

data = {"a": 1, "b": 2, "c": 3, "d": 4}
keys_to_keep = {"a", "c"}

filtered = filter_dict_by_set(data, keys_to_keep)
print("Filtered Dictionary:", filtered)

#Advanced list comprehensions
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#diagonal elements
diagonal = [matrix[i][i] for i in range(len(matrix))]

# Transpose of a matrix 
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

#Filter out rows containing negative numbers
matrix_with_negatives = [
    [1, 2, 3],
    [4, -5, 6],
    [7, 8, 9]
]
filtered_rows = [row for row in matrix_with_negatives if all(x >= 0 for x in row)]
print("Original Matrix:", matrix)
print("Diagonal:", diagonal)
print("Transpose:", transpose)
print("Filtered Rows (no negatives):", filtered_rows)

#Write a function that partitions a list into n nearly equal parts and returns a list of lists.
def partition_list(lst, n):
    result = []
    length = len(lst)
    part_size = length // n
    remainder = length % n  
    start = 0
    for i in range(n):
        end = start + part_size + (1 if i < remainder else 0)
        result.append(lst[start:end])
        start = end
    return result

numbers = [1, 2, 3, 4, 5, 6, 7]
parts = partition_list(numbers, 3)
print("Original List:", numbers)
print("Partitioned into 3 parts:", parts)

#




