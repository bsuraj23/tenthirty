# Use `map` and `filter` to get squares of even numbers from a list.
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x:x%2==0, numbers))
squares=list(map(lambda x:x*x, even_numbers))
print(squares)

