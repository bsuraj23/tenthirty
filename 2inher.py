class Mother:
 def mother_feature(self):
        print("Mother's feature")

class Father:
    def father_feature(self):
        print("Father's feature")

class Child(Mother, Father):
    def child_feature(self):
        print("Child's feature")

# Usage
c = Child()
c.mother_feature()
c.father_feature()
c.child_feature()