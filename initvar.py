class Student:  
  def __init__(self, name, grade):
    self.name = name
# instance varible
    self.grade = grade
# instance varible
  
  def show(self):
    print("Name:", self.name)
    print("Grade:", self.grade)

    # Creating an object
    s1 = Student("Alice", 8)
    s1.show()