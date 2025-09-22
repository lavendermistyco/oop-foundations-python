class BankAccount:
    def __init__(self):
        # TODO: Initialize account_number, owner_name, and balance

    def deposit(self, amount: float):
        # TODO: Add amount to balance, with input validation

    def withdraw(self, amount: float):
        # TODO: Subtract amount from balance, with input validation
    def get_balance(self):
        # TODO: Return the current balance


if __name__ == '__main__':
    acct = BankAccount('ABC-123', 'Faith', 100.0)
    acct.deposit(50)
    try:
        acct.withdraw(200)
    except ValueError as e:
        print('Withdraw failed:', e)
    print('Balance:', acct.get_balance())
