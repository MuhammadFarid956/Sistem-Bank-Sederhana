import accounts
import operational

class BankSystem:
    def __init__(self):
        self.accounts = operational.BankStorage.load_data()

    def create_account(self):
        print("[ Create Account ]")
        name = input("Enter Account Name : ")
        try:
            deposit = float(input("Enter Deposit Amount : $"))
            if deposit < 0:
                print("Deposit Amount cannot be negative")
                return

            new_account = accounts.Account(name, deposit)
            self.accounts[new_account.acc_num] = new_account
            operational.BankStorage.save_data(self.accounts)
            print(f"Success: Account Created\nNumber Account : {new_account.acc_num}")
        except ValueError:
            print("Error: Invalid Input")

    def access_account(self):
        print("[ Python Bank ]")
        num = input("Enter Account Number : ")
        acc = self.accounts.get(num)

        if not acc:
            print("Account Not Found")
            return

        while True:
            print(f"\nWelcome, {acc.acc_name}")
            print(f"Balance : {acc.acc_balance:.2f}")
            print("\n1. Deposit\n2. Withdraw\n3. Back")

            choice = input("Enter Choice : ")

            if choice == "1":
                try:
                    amount = float(input("Enter Deposit amount : $"))
                    if acc.deposit(amount):
                        operational.BankStorage.save_data(self.accounts)
                        print(f"Success: Account Deposited\n Your Balance : {acc.acc_balance:.2f}")
                    else:
                        print("Amount Not Valid")
                except ValueError:
                    print("Error: Invalid Input")
            elif choice == "2":
                try:
                    amount = float(input("Enter Withdraw amount : $"))
                    if acc.withdraw(amount):
                        operational.BankStorage.save_data(self.accounts)
                    else:
                        print("Something went wrong")
                except ValueError:
                    print("Error: Invalid Input")
            elif choice == "3":
                break

    def run(self):
        while True:
            print("\n====== PYTHON BANK ======")
            print(f"1. Create Account\n2. Access Account\n3. Exit\n")

            select = input("Enter Choice :")

            if select == "1":
                self.create_account()
            elif select == "2":
                self.access_account()
            elif select == "3":
                print("Thank You.")
                break
            else:
                print("Invalid Input.")
        return select


