try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print(" Index out of range.")
    #example 2
try:
   print(10/0)
except ZeroDivisionError:
    print("cannot divided by zero")

# example 3 
try:
    int(xyz)
except Exception as e:
    print("exception:",e)

# example 4
try:
    num=5
except:
    print("error occured")
else:
    print("no exception,num",num)    

# example 5
try:
    result=5+5
except:
      print("error")
else:
    print("result",result)