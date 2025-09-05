freom# #logical 
# n=int(input("enter a number"))
# print(n>0 and n%2==0)
#
def vote_eligible(age):
    if age >=18:
        return True
    else:
        return False
print(vote_eligible(20))