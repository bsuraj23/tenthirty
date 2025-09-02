#simple interest local variable
def simple_interest():
    principle=1000
    rate=5
    time=2
    interest=(principle*rate*time) / 100
    print("simpleinterest:",interest)
simple_interest()    

# local vaiable marks
def average():
    marks1=80
    marks2=90
    marks3=85
    average=(marks1+marks2+marks3)/3
    print("Average:",average)
average()

#local variable
def power():
    base = 2  
    exponent = 3  
    result = base ** exponent  
    print("Power Result:", result)

power()


#local varible circle with return function
def area_circle():
    pi=3.14
    radius=7
    area=pi*radius*radius
    return area
result=area_circle()
print("area of circle:",result)

#local variables
def marks():
    maths = 90
    science = 85
    return maths, science  # returning two values
m1, m2 = marks()
print("Maths:", m1)
print("Science:", m2)

# global variable
name = "Sumanth"  # Global variable
def greet():
    print("Hello", name)  # Accessing global variable inside the function
greet()
print("Outside function:", name)


#global variable
name="apple"
def greet():
    print("hello:",name)
greet()
print("ouside function:",name)

#global example 2
score=0
def update_score():
    global score
    score +=10
    print("score inside function:",score)
update_score()
print("final score:",score)

#global example3
a=8
b=5
def power():
    return a**b
result=power()
print("result of power:",result)

# global exammple 4
x=5
y=6
def multiply():
    return x*y
result=multiply()    
print("multiplication",result)

#global example 5
x = 100  
def test():
    x = 50 
    print("Inside function:", x)
test()
print("Outside function:", x)

#global example 6
x = 5
y = 10

def update_and_add():
    global x, y
    x = x + 2
    y = y + 3
    print("Updated x + y =", x + y)

update_and_add()
print("New x:", x)
print("New y:", y)


#global example 7
base = 3
exponent = 4
def power():
    result = base ** exponent
    print("Power Result:", result)
power()


# math.pow function()
import math
def power():
    x = 5
    y = 2
    result = math.pow(x, y)
    print("Power using math.pow():", result)
power()


#lambda function examples

  # lambda function
add = lambda a,b: a+b
print("sum:",add(5,7))
sub=lambda c,d: c-d
print("sub:",sub(10,5))
mult=lambda e,f: e*f
print("mult:",mult(5,5))
div=lambda g,h: g/h
print("div:",(5/5))


#example 1
square=lambda x:x*x
print("square:",square(6))

# example 2
maximum=lambda x, y:x if x>y else y  
print("maximum:",maximum(5,9))
minimum=lambda x,y:x if x<y else y
print("minimum:",minimum(7,90))


# example 3
nums=[1,4,6,9]
squares=list(map( lambda x:x**2,nums))
print("squares:",squares)

# example 4
nums=[1,2,3,4,5,6]
evens=list(filter(lambda x:x%2==0,nums))
print("evens:",evens)
nums=[1,2,3,4,5,6]
odds=list(filter(lambda x:x%2!=0,nums))
print("odds number:",odds)

# example 5
is_positive=lambda x:x>0
print("is 10 positive?",is_positive(10))
print("is -4 positive?",is_positive(-4))
# example 6
mult=lambda a,b,c:a*b*c
print("multiplication",mult(2,4,5))

# example 7
celious=[0,10,20,30,50]
fahrenheit=list(map(lambda c:(c*9/5)+32,celious))
print("fahrenheit:",fahrenheit)

# example 8
is_odd = lambda x: "Odd" if x % 2 else "Even"

for i in range(1, 6):
    print(i, "is", is_odd(i))

# example 9
numbers = [1, 2, 3, 4, 5, 6]
count_odds = len(list(filter(lambda x: x % 2 != 0, numbers)))
print("Total odd numbers:", count_odds)
    











  

















    














