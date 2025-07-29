class Example:
    @staticmethod
    def greet():
        print("Hello from static method")
    def add():
        print(90+90)
Example.greet()       #no need to create object variable if we use @staticmethod
Example.add()