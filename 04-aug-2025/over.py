# class demo:
#     def greet(self):
#         print("hello !")
#     def greet(self):
#         print("hi there")


# demo().greet()

#class example no support for overloading 

# class calc:
#     def add(self,a,b):
#         return a + b
#     def add(self,a,b,c):
#         return a + b + c
# print(calc().add(12,1))
# print(calc().add(13,14,13))


#solution
def add(*args):
    total = 0 
    for num in args:
        total += num
    print(total)

add(1,2)
add(2,3,4,5)


# class Class10:
#     def greet(self, name = None):
#         if name: 
#             print(f"hello, {name}")
#         else:
#             print("hello !")

# Class10().greet()
# Class10().greet("alice")