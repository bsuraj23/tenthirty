s = "uday kumar"
reversed_s = " "
for i in s:
    reversed_s = i + reversed_s
print(reversed_s)

#largest number
list = [10,54,65,6786,498,212,789,7898,124]
large=list[0]
for i in list:
    if i>large:
        large = i
print(large)

#vowles
s="udaykumarkotha"
count=0
vowles="aeiouAEIOU"
for i in vowles:
    count+=1
print(count)

#prime
num=45
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"not a prime")
            break
    else:
        print(num,"is a prime")
else:
    print(num,"not a prime")    