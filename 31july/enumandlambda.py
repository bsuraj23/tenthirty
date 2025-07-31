team =['mi','rcb','srh','csk']

for index,team in(enumerate(team, start=1)):
    print(index,team)
    
add = lambda x, y: x + y
print(add(3, 5)) 

square = lambda x: x * x
print(square(5))

numbers=[1,2,3,4,5]
squared = list(map(lambda x: x * x, numbers))
print(squared)
