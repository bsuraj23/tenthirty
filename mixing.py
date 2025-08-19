import math, random, datetime

radius = random.randint(1, 10)
area = math.pi * (radius**2)
print(f"Radius: {radius}, Area: {area:.2f}")

print("Generated on:", datetime.datetime.now())
