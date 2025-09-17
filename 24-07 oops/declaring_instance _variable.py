class Student:        #here this is the class inside the class we can write the code and access it with declaring object
    def __init__(self,name):   #here we defining the intialization of the class and the init method also called constructure
    #and self is the mandatory for the init method and it is the first parameter or first argument for the init method
        self.name=name       #self.name is the instance variable
    def set_age(self,age):   #here we defining a function that has self and age as parameters and self is the object instance of the class
        self.age=age    #self.age is instance variable here self makes that sure each object keeps its own data

obj=Student("john")  #here we creating a object for Student class, we need to access the class by declaring the object and dont need to 
#mention the constructure when we declaring values for the init method because it is a constructure
obj.set_age(22)   #we need to mention the function with the object because we stored the class in this obj and setting the
#values for the function parameters. 
obj.age=20    #here we assigning the age using obj and attribute of age
print(obj.name)   #here we printing the name of student class
print(obj.age)     #It prints student age
