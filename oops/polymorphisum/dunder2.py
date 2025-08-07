#dunder means double underscore
#They allow you to define or customize the behavior of your classes with respect to:

# Object construction (__init__)
# String representation (__str__, __repr__)
# Length (__len__)
# Operator overloading (__add__, __sub__, etc.)
# Comparison (__eq__, __lt__, etc.)
# Iteration (__iter__, __next__)
# Context management (__enter__, __exit__)


class Demo:
    a=90
print(Demo.__dict__)

