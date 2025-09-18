#Reverse a string without using slicing
s='hello'
rev=''.join(reversed(s))
print(rev)

#find the largest number in a list 
nums=[1,2,3,5]
print(max(nums))

#count vowels in a string
s='hello world'
vowels='aeiou'
count=sum(1 for ch in s if ch in vowels)
print(count)

#Check if a number is prime
num = int(input("Enter a number: "))

if num > 1: 
    for i in range(2, num): 
        if num % i == 0:
            print(num, "is NOT a prime number")
            break
    else:  
        print(num, "is a prime number")
else:
    print(num, "is NOT a prime number")