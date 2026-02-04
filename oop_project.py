from bank_accounts import *

Udin = BankAccount(1000, "Udinn")
Asep = BankAccount(2000, "Asep")

Udin.getBalance()
Asep.getBalance()   

Udin.deposit(500)

Udin.withdraw(500)

Udin.transfer(50, Asep)
# Udin.getBalance()
# Asep.getBalance()

