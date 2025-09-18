#static variable using constructor
class Example:
    static_var=20
    def __init__(self,name):
        self.name=name
        print(Example.static_var)
e=Example("Sindhu")

#Access outer class static variable from inner class
class Outer:
    static_var = 42   
    class Inner:
        def show(self):
            print("Outer static var:", Outer.static_var)
inner_obj = Outer.Inner()
inner_obj.show()

#Access outer class instance variable from inner class
class Outer:
    def __init__(self, name):
        self.name = name

        self.inner = self.Inner(self)

    class Inner:
        def __init__(self, outer_instance):
            
            self.outer = outer_instance

        def show_outer_name(self):
            print("Outer instance name:", self.outer.name)

o = Outer("Sindhu")
o.inner.show_outer_name()
