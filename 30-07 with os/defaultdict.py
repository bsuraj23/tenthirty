from collections import defaultdict
dd=defaultdict(int)
dd['apple']+=2
dd['banana']+=1
dd['papaya']+=4
print(dd)
print(dd['mango'],dd)  #it prints 0
