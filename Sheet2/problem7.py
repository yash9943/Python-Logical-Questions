'''
Create a BankAccount class with methods: deposit, withdraw, balance.
- Ensure balance never goes negative.
'''

class bankAccount():
    def __init__(self,bank_balance=0):
        self.balance=bank_balance
    
    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print(f"Deposit amount {amount}, New balance {self.balance}")
        else:
            print('Deposit amount must be positive.')
        
    def withdraw(self, amount):
        if amount <= 0:
            print('Deposit amount must be positive.')
        elif amount > self.balance:
            print(f"In sufficient Fuds !, Available Funds {self.balance}")
        else:
            self.balance -= amount
            print(f"Deposit withdraw {amount}, New balance {self.balance}")
    
    def get_balance(self):
        return self.balance
        
acc = bankAccount(100)
acc.deposit(50)
acc.withdraw(20)
print("Your Current balance is :",acc.get_balance())