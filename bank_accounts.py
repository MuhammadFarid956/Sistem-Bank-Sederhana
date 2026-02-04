class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit Completed.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry, account '{self.name}'  only has a balance of ${self.balance:.2f}")
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")
    
    def transfer(self, amount, account):
        try:
            print(f"\n**********\n\nBeginning Transfer")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\Transfer Complete!\n\n**********")
        except BalanceException as error:
            print(f"\Transfer Interrupted: {error}")
             
      