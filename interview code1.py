#reverse a string without using slicing
s="hello"
rev="".join(reversed(s))
print(rev)
#find the largest number in list
num=[2,4,3,6]
print(max(num))
#count vowels in string
string=input("enter a string:").lower()
vowels='aeiou'
print("vowels in the string")
for char in string:
     if char in vowels:
         print(char,end='')
#vowels         
string='hello'.lower()
vowels='aeiou'
print('vowels in the string')
for char in string:
    if char in vowels:
        print(char,end='')
#check if number is prime
num=int(input("enter a number"))
for i in range(2,num):
    if num% i==0:
        print(num,"not a prime number")
        break
    else:
        print(num ,"is a prime number")
else:
        print(num, "is not a number")
#
n=17
if n>1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("not prime")
            break
        else:
            print("prime")
    else:
        print("not prime")
#
def is_prime(n):
    if n<1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(is_prime(7))
print(is_prime(35))  
