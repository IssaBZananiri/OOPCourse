'''
Bank Account Management
Author: Issa B. Zananiri 26/11/2023
Classes: Bank, Bank Account
'''

class Bank:
    # initialize the set of bank accounts
    def __init__(self):
        self.bankaccounts =[]
    
    # add bank accounts
    def add_bank_account(self, bankaccount):
        self.bankaccounts.append(bankaccount)

    # retreive bank accounts    
    def retrieve_bank_account(self,bankaccount):
        for i in self.bankaccounts:
            if i == bankaccount:
                return bankaccount
            

class BankAccount:
    # Initialize the Class 
    def __init__(self, customer_name, account_number ,initial_balance):
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = initial_balance
    
    # Deposit in the Bank Account
    def deposit_account(self, amount_deposit):
        self.balance = self.balance + amount_deposit
    
    def withdraw_account(self, amount_withdraw):
        if amount_withdraw > self.balance:
            print("Cannot withdraw that amount, the MAximum you can is: {}".format(self.balance))
        
        else:
            self.balance = self.balance - amount_withdraw
    
    def check_balance(self):
        print("Your Balalnce for Account Number {} is {}".format(self.account_number, self.balance))




issa_account = BankAccount("Issa Zananiri", 253, 5000)
hapoalimBank = Bank()
hapoalimBank.add_bank_account(issa_account)


issa_account.check_balance()
issa_account.deposit_account(1000)
issa_account.check_balance()
issa_account.withdraw_account(2000)
issa_account.check_balance()





        
        