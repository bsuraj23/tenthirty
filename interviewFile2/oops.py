class car :
    def info(self, brand, model="harrier"):
        self.brand= brand
        self.model= model
        
    def show(self):
        print(f"car brand is {self.brand} and model is {self.model}")
        
c= car()
c.info("tata","nexon")
c.show()

#initialization 

class abc:
    def info(self ,name, age=18, city= "hyderabad"):
        self.name= name
        self.age= age
        self.city= city
 
a= abc
a.name= "soham"
a.age= 22
a.city= "amravati"

print(a.name)
print(a.age)
print(a.city)        


#polyphormism


class dog:
    def sound(self ):
        return "bark"
    
class cat:
    def sound(self):
        return "meow"
    
d = dog()
print(d.sound())

c= cat()
print(c.sound() )   
        
        