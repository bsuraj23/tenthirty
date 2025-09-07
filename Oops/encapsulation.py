class Account:
    def __init__(self):
        self.balance=0
    def deposit(self, amount):
        self.balance=self.balance+amount
    def show(self):
        print("Balance:",self.balance)

acc=Account()
acc.deposit(100)
acc.show()


