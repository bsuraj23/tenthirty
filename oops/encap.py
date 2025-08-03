#parent class
class Dog:
    def __init__(self,name,breed,age):
        self.name=name #Public attribute
        self._breed=breed #Protected attribute
        self.__age=age #Private attribute
    
    #Acessing public attribute
    def get_info(self):
        return f"Dog Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"
    
    #Returns age using setter method in private attribute
    def set_age(self,age):
        if age > 0:
            self.__age=age
        else:
            return "Age is not valid"
        
    # Returns age using getter method in private attribute
    def get_age(self):
        return self.__age
    
dog=Dog("Bobby","Labrador",5)
# Accessing public attribute
print(dog.name)
# Accessing protected attribute but within the same class
print(dog._breed)
# Accessing private attribute 
print(dog.get_age())
dog.set_age(6)
print(f"Updated dog info after changing age , {dog.get_info()}")
            