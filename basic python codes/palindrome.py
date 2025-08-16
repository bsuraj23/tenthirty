n=int(input("Enter the number:"))
original=n
rev=0
while n>0:
    rem=n%10
    n=n//10
    rev=rev*10+rem
if original==rev:
    print("Palindrome")
else:
    print("Not palindrome")