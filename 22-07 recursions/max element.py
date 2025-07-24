def maxi(n):
    if len(n)==1:
        return n[0]
    return max(n[0], maxi(n[1:]))
print(maxi([1,3,4,5,6,2,9,6,7,8]))

