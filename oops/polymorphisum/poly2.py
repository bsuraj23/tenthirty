class Demo:
    def show(self,a=0,b=0):
        if a and b:
            print(a,b)
        elif(a):
            print(a)
        else:
            print("No values provided")

obj=Demo()
obj.show(10,20)  # Output: 10 20
obj.show(10)  # Output: 10
obj.show()  # Output: No values provided