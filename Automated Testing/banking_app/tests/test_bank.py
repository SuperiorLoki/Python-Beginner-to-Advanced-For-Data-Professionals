import pytest
from src.bank import BankAccount

def test_create_account():
    account = BankAccount("HP", 100)
    assert account.owner == "HP"
    assert account.balance ==100

def test_deposit():
    account = BankAccount("Curry")
    account.deposit(50)
    account.deposit(50)
    assert account.balance == 100

    with pytest.raises(ValueError):
        account.deposit(-10)

def test_withdraw():
    account = BankAccount("Andrew", 100)
    account.withdraw(40)
    assert account.balance == 60

    with pytest.raises(ValueError):
        account.withdraw(200)

#to skip certain tests
@pytest.mark.skip(reason = "Due to Construction.")
def test_get_balance():
    account=BankAccount("MJ", 200)
    assert account.get_balance() == 200