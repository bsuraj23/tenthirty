row =  5
for i in range(1, row+1):
    print(" "*(row-i)+"* "*i)
for j in range(row-1,0,-1):
    print(" "*(row-j)+"* "*j)

row = 5
for i in range(1, row+1):
    print(" "*(row-i)+"* "*i)  #or  print(" "*(row-i)+(2*i-1)*"*")
for j in range(row-1,0,-1):
    print(" "*(row-j)+"* "*j)  #0r  print(" "*(row-i)+(2*i-1)*"*")

