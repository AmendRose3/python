# 60. Create a Python program that simulates a bank account system. The base class
# `Account` should have attributes like `account_number`, `account_name`, and
# `balance`. It should include deposit and withdraw methods that update the balance
# accordingly. Derive two subclasses from `Account`: `SavingsAccount` and
# `CheckingAccount`. Add a unique feature to each subclass, such as a
# `minimum_balance` requirement for `SavingsAccount` and a `write_check()` method
# for `CheckingAccount`. Ensure proper usage of inheritance and encapsulation
# principles.
class Account:#Base class
    def __init__(self,account_number,account_name,balance):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=balance
    def deposit(self,money):
        print(f"Current Balance: {self.balance}")
        self.balance+=money
        print("Deposit Successful")
        print(f"New Balance: {self.balance}")
    def withdraw(self,minimum_balance,money):
        print(f"Current Balance: {self.balance}")
        if((self.balance-minimum_balance)>money ):
            self.balance+=money
            print("Withdraw Successful")
            print(f"New Balance: {self.balance}")
        else:print("Withdraw Unsuccessful-Check your Balance or exceeding minimum balance")
        
class SavingsAccount(Account):
    minimum_balance=1000
    def __init__(self, account_number, account_name, balance=0):
        super().__init__(account_number, account_name, balance)
    def withdraw(self,money):
        super().withdraw(minimum_balance,money)
    def deposit(self,money):
        super().deposit(money)
        
class CheckingAccount(Account,):
        def __init__(self, account_number, account_name, balance=0):
            super().__init__(account_number, account_name, balance)
        def write_check(self,money):
            print(f"Signed Check for Rs: {money}")
            print(f"proceeding withdrawal....")
            super().withdraw(self,1000,money)




