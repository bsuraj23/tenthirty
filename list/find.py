list=["1",2,23,45.321,"Manish"]
a=input("Enter a value to find in the list: ")
if a in list:
    i=list.index(a)
    list[i]="Kumar"
    print(list)
else:
    print(f"{a} is not in the list")