i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

#continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

 # pass   
for i in range(5):
    if i == 2:
        pass
    else:
        print("i=",i)
