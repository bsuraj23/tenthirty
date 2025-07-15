for i in range(100,200):
    h=i//100
    t=(i//10)%10
    u=i%10
    if h==t or t==u or h==u:
        print(i, end=' ')
        
print("\nThe numbers with repeated digits between 100 and 200 listed above.")