for match in range(1,2):
    for overs in range(1,21):
        print(match,"match",overs,"over")


print("Here we are using break statement")
for j in range(1,6):
    if j==3:
        break
    print(j)


print("Here we are using pass statement")
for k in range(1,6):
    if k==3:
        pass
    print(k)

print("Here we are using continue statement")
for l in range(1,6):
    if l==3:
        continue
    print(l)       