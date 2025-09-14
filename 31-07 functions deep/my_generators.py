#simple generator
def my_generator():
    yield 1
    yield 2
    yield

gen = my_generator()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
#print(next(gen))    # It will raise StopIteration


#generator in a loop
def countdown(n):
    while n>0:
        yield n
        n=n-1

for num in countdown(5):
    print(num)



    