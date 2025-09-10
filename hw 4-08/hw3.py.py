class Calculator:
    def add(self, a, b):
        print("Add with 2 arguments:")
        return a + b

    def add(self, a, b, c):
        print("Add with 3 arguments:")
        return a + b + c

# Create object
calc = Calculator()
print(calc.add(10, 20, 30)) 