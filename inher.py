class Grandparent:
     def grandparent_feature(self):
        print("Grandparent's feature")

class Parent(Grandparent):
    def parent_feature(self):
        print("Parent's feature")

class Child(Parent):
    def child_feature(self):
        print("Child's feature")

# Usage
c = Child()
c.grandparent_feature()
c.parent_feature()
c.child_feature()