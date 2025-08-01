from collections import Counter
count=Counter(['apple','banana',1,'banana',2,'mango','apple',1])
print(count)
print(count['apple'])
print(count.most_common(3))