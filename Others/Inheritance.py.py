class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")
    
class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def show_school(self):
        print(f"I study at {self.school}")
 
class CollegeStudent(Student):
    def __init__(self, name, school, course):
        super().__init__(name, school)
        self.course = course

    def show_course(self):
        print(f"I am enrolled in {self.course} course")
        
        
        
cs = CollegeStudent("MR<Sunil", "MEADHA EDU TECH", "PYTHON FULL STACK")
cs.greet()
cs.show_school()
cs.show_course()
