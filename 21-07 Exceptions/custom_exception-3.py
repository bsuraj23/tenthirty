class BalanceError(Exception):
    def __init__(self, balance, message="Insufficient balance."):
        self.balance=balance
        self.message=message
        super().__init__(self.message)
    
try:
    balance=200
    withdraw=500
    if withdraw>balance:
        raise BalanceError(balance,"The withdraw is more than your balance.")
    print("Successful withdraw")
except BalanceError as a:
    print(f"Error: {a.message} current balance: {a.balance}")
