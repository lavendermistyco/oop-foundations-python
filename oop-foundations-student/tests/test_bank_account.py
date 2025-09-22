import pytest
from examples.bank_account import BankAccount

def test_deposit_and_balance():
    acct = BankAccount('XYZ', 'Faith', 10.0)
    acct.deposit(15.0)
    assert acct.get_balance() == 25.0

def test_withdraw_success():
    acct = BankAccount('XYZ', 'Faith', 100.0)
    acct.withdraw(40.0)
    assert acct.get_balance() == 60.0

def test_withdraw_insufficient_funds():
    acct = BankAccount('XYZ', 'Faith', 10.0)
    with pytest.raises(ValueError):
        acct.withdraw(50.0)
