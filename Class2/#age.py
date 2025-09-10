#age
# age = 20
# if age <5:
#     print("eligible to enter")
# else:
#     print("not eligible")

#     #swapping with third variable
# a=2
# b=4
# c=6
# print("before swapping")
# print("a=", a)
# print("b=", b)
# print("c=", c)
# temp=a
# a=b
# b=c
# c=temp
# print("after swapping")
# print("a=", a)
# print("b=", b)
# print("c=", c)
# #swap without third variable
# a=2
# b=4
# a,b=b,a
# print("a", a)
# print("b", b)
# #using type
# a=2
# b=0.23
# c="ant"
# d=False
# e=(2,1,3)
# f=[23]
# g={1,2,3}
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
#take input as user and print a greeting message
# name=input("enter the name")
# print("hello",name+"#"+" welcome")
#input two numbers and print their sum, difference and product

# num1=int(input("enter a first num"))
# num2=int(input("enter a second num"))
# print("sum", num1+num2)
# print("difference", num1-num2)
# print("product", num1*num2)
# print("quotient", num1/num2)

#check even and odd
# num=12
# if num % 3==0:
#     print("even")
# else:
#     print("odd")
#check if a number is postive,negative or zero
# num=int(input("enter a num"))
# if num >0:
#     print("positive")
# elif num <0:
#     print("negative")
# else:
#     print("zero")

#find the largest of three numbers
num1=int(input("enter the first num"))
num2=int(input("enter the second num"))
num3=int(input("enter the third num"))
if num1 >= num2 and num1 >= num3:
    largest=num1
elif num2 >= num1 and num2 >=num3:
    largest=num2
else:
    largest=num3
    print("the largest number is", largest)