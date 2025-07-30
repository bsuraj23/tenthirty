
y = int(input("enter your year"))
# if (y%4 == 0):
#     if (y % 100 == 0):
#         if (y % 400 == 0):
#             print("yes it's a leap year")
#         else:
#             print("it's not a leap year")
    
#     else:
#         print("yess it's a leap year")
# else:
#     print("it's not a leap year")

#with package

import calendar 


if calendar.isleap(y):
    print(y,"It's a leap year")
else:
    print(y,"it's not a leap year")