import random

class Account:
    def __init__(self, account_name, initial_deposit, account_num= None):
        self.acc_name = account_name
        self.acc_balance = float(initial_deposit)
        self.acc_num = account_num if account_num else self.gen_acc_num()

    def gen_acc_num(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])

    def deposit(self, amount):
        if amount > 0:
            self.acc_balance += amount
            print(f"Deposited ${amount}. New balance : ${self.acc_balance:.2f}")
            return True
        print("Invalid deposit amount.")
        return False

    def withdraw(self, amount):
        if 0 < amount < self.acc_balance:
            self.acc_balance -= amount
            print(f"Withdrew ${amount}. New balance : ${self.acc_balance:.2f}")
            return True
        print("Invalid withdrawal amount or insufficient founds")
        return False

    def transfer(self, amount, recipient):
        if recipient == self:
            print("Error: Can't transfer to own account")
            return False
        if amount <= 0:
            print("Error: Transfer amount cannot be negative")
            return False
        if self.withdraw(amount):
            recipient.deposit(amount)
            print(f"Transfer ${amount} to {recipient.acc_name} successful")
            return True
        else:
            print("Transfer Failed")
            return False

    def to_list(self): #Konversi data to CSV file
        return [self.acc_num, self.acc_name, self.acc_balance]