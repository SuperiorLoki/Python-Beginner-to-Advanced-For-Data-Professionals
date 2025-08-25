class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit Amount Must be Positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient Funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

my_account = BankAccount("HP")



