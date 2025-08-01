# Print Right-Angled Triangle Using 

rows = 5
for i in range(1, rows + 1):
    print("*" * i)

#2. Check Triangle Type (Equilateral, Isosceles, Scalene)

a = 5
b = 5
c = 5

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

#3. Calculate Area of Triangle

import math

a = 3
b = 4
c = 5

s = (a + b + c) / 2  # semi-perimeter
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("Area of triangle is:", area)