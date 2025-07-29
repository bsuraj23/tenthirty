n=[1,2,2,3,4,5,5,6,"m","ma","ma"]
same=[]
for i in n:
    if i not in same and n.count(i) > 1:
        same.append(i)
print("Repeated elements:", same)