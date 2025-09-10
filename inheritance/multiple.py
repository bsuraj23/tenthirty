#example1
# Parent class 1
class Father:
     def skills(self):
         print("Gardening, Programming")

 # Parent class 2
class Mother:
     def skills(self):
         print("Cooking, Art")

 # Child class inheriting from both
class Child(Father, Mother):
     def skills(self):
         Father.skills(self)
         Mother.skills(self)
         print("Dancing, Singing")

c = Child()
c.skills()

#example2
class Teacher:
    def teach(self):
        print("Teaches subjects")

class Parent:
    def care(self):
        print("Takes care of children")

class Student(Teacher, Parent):
    def study(self):
        print("Studies hard")

s = Student()
s.teach() 
s.care()   
s.study() 