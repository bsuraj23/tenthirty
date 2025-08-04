class Parent:
    def greet(self):
        print("hello from parent ")
        
class Child(Parent):                # simple example 
    def greet(self):
        print("hello from child ")
        
objA= Child()
objA.greet()        
     
     
class Dog:
    def speak(self ):
        print("Bark")
   
class Cat:
    def speak(self):
        print("meow")
        
def func(animal):
    print(animal.speak())
    
dog= Dog()
cat= Cat()

func (dog)
func(cat)                        