#reversing a string without using slicing
s="dheeraj"
reversed_s=" "
for i in s:
    reversed_s=i+reversed_s
print(reversed_s)


#Find the largest number in a list.
list=[10,11,234,244,2345,123,456]
largest=list[0]
for i in list:
    if i>largest:
        largest=i
print(largest)


#Count vowels in a string.
s="areoplane"
count=0
vowels="aeiouAEIOU"
for i in s:
    if i in vowels:
        count+=1
print(count)


#Write a program to check if a number is **prime**.
num=29
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")