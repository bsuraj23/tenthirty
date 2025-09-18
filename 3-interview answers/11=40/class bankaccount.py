#  Create a class `BankAccount` with methods `deposit`, `withdraw`, and `check_balance`.class BankAccount:
def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")

def check_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance


# Example usage
account = BankAccount("Alice", 1000)
account.check_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
