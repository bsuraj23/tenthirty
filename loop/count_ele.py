# from collections import Counter 
# n=[1,2,3,3,2,3,1,"mam","mam","man"]
# freq={}

# c=Counter(n)
# print("Frequency of elements in the list:")
# for key, value in c.items():
#     print(f"{key}: {value}")

#without any built-in functions
n=["mam",1,2,3,"man",8,4,2,1]
freq={}
for i in n:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Frequency of elements in the list:")

#using a for loop to print frequency
for key, value in freq.items():
    print(f"{key}: {value}")