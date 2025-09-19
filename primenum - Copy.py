#Coding Practice (Beginner)
#Check if a number is prime.
n=7
if n>1:
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      print('Not Prime')
      break
  else:
    print('Prime or not')
