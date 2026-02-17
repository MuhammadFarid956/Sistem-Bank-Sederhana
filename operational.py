import csv
import os
from accounts import *
import datetime

FILENAME = "accounts_data.csv"

class BankStorage:
    @staticmethod
    def load_data():
        accounts = {}
        if not os.path.exists(FILENAME):
            return accounts

        try:
            with open(FILENAME, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row :
                        new_acc = Account(account_name=row[1], initial_deposit=row[2], account_num=row[0])
                        accounts[new_acc.acc_num] = new_acc
            return accounts
        except Exception as e:
            print(f"File not found: {e}")
            return{}

    @staticmethod
    def log_transaction(type_transaction, acc_num, amount, info=''):
        file_log = "transactions.csv"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(file_log, 'a', newline='') as log:
                writer = csv.writer(log)
                writer.writerow([timestamp, type_transaction, acc_num, amount, info ])
        except Exception as e:
            print(f"Cannot write log: {e}")

    @staticmethod
    def save_data(accounts_dict):
        try:
            with open(FILENAME, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(acc.to_list() for acc in accounts_dict.values())
        except Exception as e:
            print(f"File not found. Can't save data: {e}")
