class Person:
    d=10
    
    @classmethod
    def dis(cls):
        print(f"Value of d is {cls.d}")
    
Person.dis()  # Output: Value of d is 10