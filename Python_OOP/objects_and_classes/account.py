class Account:
    def __init__(self, _id: int, name: str, balance: int = 0):
        self.id = _id
        self.name = name
        self.balance = balance

    def credit(self, amount: int):
        self.balance += amount
        return self.balance

    def debit(self, amount: int):
        if self.balance > amount:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"
