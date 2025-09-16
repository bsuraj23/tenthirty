total_sum = 0
#lo#start with total sum = 0
#loop through 1 to 1000
for i in range(1, 1001):
    #check if divisible by 3 or 5
    if i % 3 == 0 or i  % 5 == 0:
       # if so, add to the total sum
      total_sum += i
    print("sum of multiple of 3 and 5 is ,is 1000", total_sum)
    print(total_sum)



    #start with total sum = 0
total_sum = 0
    #loop through 1 to 900
for i in range(1, 999):  # Use 1000 to match Euler's "below 1000"
        #check if divisible by 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            # if so, add to the total sum
            total_sum += i
print("Sum of multiples of 3 and 5 below 1000 is", total_sum)
#fibonacci question 
x, y = 1,2
total = 0
while x < 4000000:
    if x % 2 == 0:
        total += x
    x, y = y, x + y


