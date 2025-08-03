n = int(input("Enter a number: "))
count = 0
# First, count the number of digits
t = n
while t > 0:
    count += 1
    t //= 10

# Now compute the sum of digits raised to 'count'
dig = 0
# Reset t to the original number
t=n
while t > 0:
    r = t % 10
    dig += r ** count
    t //= 10

# Check Armstrong condition
if n == dig:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")