class Mobile:
    def __init__ (self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price

    def config(self):
        print("The brand is :",self.brand, self.model, self.price)
        
mbl1=Mobile('Realme', 'gt2pr0',60000)
mbl2=Mobile('Redmi','note10',40000)

mbl1.config()
mbl2.config()











