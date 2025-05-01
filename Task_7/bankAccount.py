class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = balance

    def Deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def bankFees(self):
        fee = 0.05 * self.balance
        self.balance -= fee

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Name: {self.name}")
        print(f"Account Balance: {self.balance} $")