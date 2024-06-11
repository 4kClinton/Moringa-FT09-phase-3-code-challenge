# bank.py
class BankAccount:
    def _init_(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount")

class SavingsAccount(BankAccount):
    def _init_(self, account_number, owner, balance=0, interest_rate=0.01):
        super()._init_(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate

class CheckingAccount(BankAccount):
    def _init_(self, account_number, owner, balance=0, overdraft_limit=100):
        super()._init_(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and (self._balance + self.overdraft_limit) >= amount:
            self._balance -= amount
        else:
            raise ValueError("Overdraft limit exceeded or invalid withdrawal amount")