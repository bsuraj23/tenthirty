
number = [1,2,3,4,5]


for temp in number:
    if all(temp%2==0):
        print("found even number")
    else:
        print("Not even")