'''
Sometimes, you want to throw an error if something that you don't want happens
'''

#Creating a custom exception
class InsufficientFunds(Exception):
    pass

balance = 0

def deposit(amount):
    #Need to access the balance variable inside this funciton, so need to make it global
    global balance
    if amount <= 0:
        #Throw an error
        raise ValueError("Amount must be positive for deposit")
    else:
        balance += amount

def withdraw(amount):
    global balance
    if amount > balance:
        raise InsufficientFunds(f"Not enough funds. Current balance {balance}")
    balance -= amount

deposit(10)
withdraw(5)
print("Money left in my bank account: ", balance)
