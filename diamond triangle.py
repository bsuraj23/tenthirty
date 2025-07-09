row = 5
for i in range(1, row+1):
    print(" "*(row-i)+"* "*i)  #or  print(" "*(row-i)+(2*i-1)*"*")
for j in range(row-1,0,-1):
    print(" "*(row-j)+"* "*j)  #0r  print(" "*(row-i)+(2*i-1)*"*")

#using while loop
print("-->While loop")
n=5
i=1
while i<=n:
    print(" "*(n-i)+(2*i-1)*"*")
    i=i+1
i=n-1
while i>=1:
    print(" "*(n-i)+(2*i-1)*"*")
    i=i-1

