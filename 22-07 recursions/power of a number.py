def power(base,expo):
    if expo==0:
        return 1
    return base*power(base,expo-1)
print(power(4,4))