#Bank account class with deposit, withdraw, and balance 
class BankAccount:
    def __init__(self,owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs.{amount}. New Balance: Rs.{self.balance}")

    def withdraw(self,amount):
        if amount> self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn Rs.{amount}. New balance: Rs.{self.balance}")
        
    def check_balance(self):
        print(f"Current balance: Rs{self.balance}")

acc = BankAccount("Deepthi", 10000)
acc.deposit(5000)
acc.withdraw(2000)
acc.check_balance()

