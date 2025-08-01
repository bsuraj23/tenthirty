# import collections
# print(dir(collections))

from  collections import Counter
cnt=Counter(['apple','banana','apple','orage'])

print(cnt)

print(cnt['apple'])

print(cnt.most_common(1)) 