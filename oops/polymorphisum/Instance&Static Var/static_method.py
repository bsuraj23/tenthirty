class Employee:
    company = "Wipro"  # Static variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
        
    def show(self):
        print(f"Employee: {self.name}, Company: {Employee.company}")
        
    @staticmethod
    def company_info():
        print(f"[Static Method]Company: {Employee.company}")

e1 = Employee("Alice")
e2 = Employee("Bob")
e1.show()  # Output: Employee: Alice, Company: Wipro
e2.show()  # Output: Employee: Bob, Company: Wipro

Employee.company = "TCS"  # Changing static variable
e1.company="ACCENTURE"  # Changing instance variable (does not affect static variable)
print("After changing static variable or shadowing ")
e1.show()  # Output: Employee: Alice, Company: TCS
Employee.company_info()  # Output: [Static Method]Company: Wipro