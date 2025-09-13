def reverse(str):
    rev=""
    for ch in str:
        rev= ch+rev
        
    return rev    

str="soham"
print(reverse("soham"))        