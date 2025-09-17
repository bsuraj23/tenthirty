numbers=[1,2,3,4,234,55,6,3,4,67,9]
even_numbers=list(filter(lambda x:x%2==0, numbers))
print(even_numbers)
#filter is used to filter elements in a collection of elements based on a condition which returns True
#eg: x = x%2==0 --> if the condition satisfies it returns the number which is satisfied
