from accounts import  Account

class Bank:
    def __init__(self):
        self.accounts = {} #Dictionary

    def create_account(self, new_account):
        name = input("Enter account holder's name : ")
        try:
            initial_deposit = float(input("Enter initial deposit amount: $ "))
            if initial_deposit < 0:
                print("Initial deposit cannot be negative")
                return
            new_acount = Account(name, initial_deposit)
            self.accounts[new_account.account_number] = new_account
        except ValueError:
            print("Invalid input for deposit. Please enter a number")

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def close_account(self):
        account_number = input("Enter account number to close : ")
        account = self.find_account(account_number)
        if account:
            print(f"closing account for {account.name}")
            del self.accounts[account_number]
            print(f"account closed successfully.")
        else:
            print("Account not found.")

