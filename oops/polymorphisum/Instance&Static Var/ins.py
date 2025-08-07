class Grades:
    def __init__(self, name, grade):
        self.name = name            # Instance variable
        self.grade = grade          # Instance variable
    def show(self):
        print( f"Name: {self.name}, Grade: {self.grade}")

s1= Grades("Alice", "A")
s2= Grades("Bob", "B+")
s1.show()  # Output: Student: Alice, Grade: A
s2.show()  # Output: Student: Bob, Grade: B+