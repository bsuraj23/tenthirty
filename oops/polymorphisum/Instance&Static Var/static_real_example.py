#@static method is same as other methods but it does not take self or cls as first argument

from datetime import date
class Person:
    def __init__(self, name, birth_year):
        self.name = name  # Instance variable
        self.birth_year = birth_year
        
    @staticmethod    
    def is_adult(age):
        return age >= 18  # Static method to check if age is adult
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)  # Class method to create instance from birth year

p= Person.from_birth_year("Alice", 1990)
print(Person.is_adult(p.birth_year))  # Output: True if age >= 18, else False