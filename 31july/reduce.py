from functools import reduce

nums1=[1,2,3,4]
sum= reduce(lambda x, y : x+y, nums1) #sum
print(sum)

nums2=[5,6,7,8]
mul= reduce(lambda x,y : x*y,nums2) #multiply
print(mul)

nums3 =[45,65,34,54]
big= reduce(lambda x, y : x if x>y  else y , nums3)
print(big)