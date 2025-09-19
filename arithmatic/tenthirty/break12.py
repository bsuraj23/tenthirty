#for loop with break
for i in range(6):
    if i==3:
     break
print(i)

#while loop wuth loop
count=0
while True:
    print("count:", count)
    count+=1
    if count==5:
       break

#for loop with list and condition
numbers=[1,3,5,7,9]
for num in numbers:
   print(num)
if num==5:
   print("found 5!")
 

   
