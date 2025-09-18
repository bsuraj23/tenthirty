# 31.What are metaclasses in Python?
# Define a metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

# Use the metaclass
class Foo(metaclass=MyMeta):
    pass
