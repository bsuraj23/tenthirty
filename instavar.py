class Student:
  def __init__(self, name, grade):
    # instance variables
    self.name = name
    self.grade = grade

def introduce(self):
  print(f"My name is{self.name} and I am in grade{self.grade}.")

  # Creating instance of the Student class
  student1 = Student("Pooja", 10)
  student2 = Student("Munni", 14)

  #Accessing instance variables
  student1.introduce()
  student2.introduce()