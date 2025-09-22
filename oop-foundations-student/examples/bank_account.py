class BankAccount:
    def __init__(self, account_number: str, owner_name: str, starting_balance: float = 0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = float(starting_balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance


if __name__ == '__main__':
    acct = BankAccount('ABC-123', 'Faith', 100.0)
    acct.deposit(50)
    try:
        acct.withdraw(200)
    except ValueError as e:
        print('Withdraw failed:', e)
    print('Balance:', acct.get_balance())
