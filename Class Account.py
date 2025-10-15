class Account:
    def __init__(self, balance):
        self._balance = balance   

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative!")

acc = Account(1000)
print(acc.balance)    

acc.balance = 2000    
print(acc.balance)

acc.balance = -500    