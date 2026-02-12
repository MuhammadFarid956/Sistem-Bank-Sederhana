import random

class Account:
    def __init__(self, account_name, initial_deposit, account_num= None):
        self.acc_name = account_name
        self.acc_balance = float(initial_deposit)
        self.acc_num = account_num if account_num else self.gen_acc_num()

    @staticmethod
    def gen_acc_num():
        return ''.join(str(random.randint(0, 9) for _ in range(10)))

    def deposit(self, amount):
        if amount > 0:
            self.acc_balance += amount
            print(f"Deposited ${amount}. New balance : ${self.acc_balance:.2f}")
            return True
        print("Invalid deposit amount.")
        return False

    def withdraw(self, amount):
        if amount > 0 and amount < self.balance:
            self.acc_balance -= amount
            print(f"Withdrew ${amount}. New balance : ${self.acc_balance:.2f}")
            return True
        print("Invalid withdrawal amount or insufficient founds")
        return False

    def to_list(self): #Konversi data to CSV file
        return [self.acc_num, self.acc_name, self.acc_balance]

    def __str__(self):
        return f"Name : {self.acc_name} | Number Account : {self.acc_num} | Balance : ${self.acc_balance:.2f}"

    # def create_acc(self, new_acc_num):
    #     self.acc_num = new_acc_num
    #     new_acc = self.to_list()
    #     self.accounts.append(new_acc)
    #     Utility.save_data()
    #     return new_acc
    #
    #
    #
    # def check_balance(self):
    #     print(f"Current balance for account {self.account_number}: ${self.balance} ")
    #
    # def display_details(self):
    #     print("\n--- Account Details ---")
    #     print(f"Account Holder : {self.name}\nAccount Number : {self.account_number}\nBalance : {self.balance}")
    #     print("-" * 30)
    #
    # # def __init__(self, name, initial_deposit):
    # #     self.name = name
    # #     self.balance = initial_deposit
    # #     self.account_number = self.generate_account_number()
    # #     print(f"Account for {self.name} created successfully.")
    # #     print(f"Your Number is: {self.account_number}")
    # #
    # # def generate_account_number(self):
    # #     # Simple generate a 10-digit account number
    # #     return ''.join([str(random.randint(0,9)) for _ in range(10)])
