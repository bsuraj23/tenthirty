#input year 
year = 2025

# leap year logic without any function
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("Year is a leap year")
        else:
            print("Year is not a leap year")
    else:
        print("Year is a leap year")
else:
    print("Year is not a leap year")

