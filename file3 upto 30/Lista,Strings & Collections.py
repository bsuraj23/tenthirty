#Lista,Strings & Collections
#6.Reverse list in place
def reverse_in_place(lst):
    i, j = 0, len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
lst=[1,2,3,4,5]
reverse_in_place(lst)
print(lst)
#7.Flatten a nested list
def flatten(nested):
    return [x for sub in nested for x in sub]
print(flatten([[1,2],[3,4],[5]]))
#8.Count Vowels/Consonants
def count_vc(s):
    vowels = set("aeiou")
    v = c = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c
print(count_vc("Hello, World!"))
#9.Second largest
def second_largest(lst):
    unique = sorted(set(lst), reverse=True)
    return unique[1] if len(unique) > 1 else None
print(second_largest([3, 1, 4, 4, 5, 5, 2]))
#10.Rotate list by k
def rotate(lst, k):
    n = len(lst)
    if n == 0:
        return lst[:]   
    k %= n
    if k == 0:
        return lst[:]  
    return lst[-k:] + lst[:-k]
print(rotate([1, 2, 3, 4, 5], 2))  
print(rotate([1, 2, 3, 4, 5], -1))  
print(rotate([], 3))