#Bank account class in python 20 Nov 2026
class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        # Enforce the rule even when the account is first created
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited R{amount:.2f}. New balance: R{self._balance:.2f}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        # Rule protection: Prevent balance from going below zero
        if amount > self._balance:
            return f"Transaction declined: Insufficient funds for {self.account_holder}."
        if amount <= 0:
            return "Withdrawal amount must be positive."
            
        self._balance -= amount
        return f"Withdrew R{amount:.2f}. Remaining balance: R{self._balance:.2f}"


# 1. Create two objects (instances of the class)
account_1 = BankAccount("Thabo Mokoena", 500.00)
account_2 = BankAccount("Lerato Ndlovu", 150.00)

# 2. Test the 'withdraw' method on both objects
print(account_1.withdraw(200.00))  # Valid transaction
print(account_2.withdraw(300.00))  # Violates the protected rule
