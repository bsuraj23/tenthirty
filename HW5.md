 1. INSTANCE METHOD (Actual Method)
Definition:An instance method is the most common type of method in a class. It takes self as the first parameter, which refers to the specific object (instance) calling the method.

Usage:
Used to access or modify instance variables of a class.

program:
class MyClass:
    def __init__(self, value):
        self.value = value

    def actual_method(self):  # also called instance method
        return f"The value is {self.value}"

obj = MyClass(10)
print(obj.actual_method())

🟢 Key Point: Needs an object to be called (e.g., obj.actual_method())

🔹 2. CLASS METHOD
Definition:A class method uses @classmethod decorator and takes cls as the first parameter, which refers to the class itself (not an instance).

Usage:
Used to access or modify class variables.
Can be called with the class name or object
program:

class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def rate_of_class_method(cls):
        return f"Total objects created: {cls.count}"

obj1 = MyClass()
obj2 = MyClass()
print(MyClass.rate_of_class_method())  # OR obj1.rate_of_class_method()

🟢 Key Point:
Works with class itself
not tied to any one instance.

| Feature           |     Instance Method (Actual Method)       | Class Method                       |
| ----------------- | ------------------------------- | ---------------------------------- |
| First argument    | `    self`                          |      `cls`                              |
| Bound to          |      Object (instance)               |     Class                              |
| Access to         |      Instance and class variables    |     Only class variables               |
| Decorator needed? |      ❌ No                            |   ✅ Yes, `@classmethod`              |
| Call via          |      `obj.method()`                  | `   Class.method()` or `obj.method()` |
