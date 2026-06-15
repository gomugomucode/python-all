class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance  # Encapsulated private attribute

    #  Standard getter method
    def get_balance(self):
        return self.__balance

    # Helper method for child classes to safely update the balance internally
    def _set_balance(self, amount):
        self.__balance = amount

    #  Validate and execute deposits
    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            print("Error: Amount must be a number.")
            return
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return
        
        self.__balance += amount

    #  Validate and execute standard withdrawals
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            print("Error: Amount must be a number.")
            return
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return
        if amount > self.__balance:
            print("Not enough balance!")
            return
        
        self.__balance -= amount


#  Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0):
        # Pass the arguments to the parent constructor
        super().__init__(name, balance)

    def add_interest(self, rate):
        if not isinstance(rate, (int, float)) or rate < 0:
            print("Error: Invalid interest rate.")
            return
        # Calculate interest using the getter, then deposit it
        interest_earned = (self.get_balance() * rate) / 100
        self.deposit(interest_earned)


#  Current Account with Overdraft
class CurrentAccount(BankAccount):
    def __init__(self, name, balance=0, overdraft_limit=0):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    # Overriding the parent withdraw method
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            print("Error: Amount must be a number.")
            return
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return
        
        # Calculate max allowable debt
        available_total = self.get_balance() + self.overdraft_limit
        
        if amount > available_total:
            print("Overdraft limit reached!")
            return
        
        # Safely update the balance using the parent's internal helper method
        new_balance = self.get_balance() - amount
        self._set_balance(new_balance)


# --- SAMPLE RUN TEST ---

print("--- Savings Account ---")
s = SavingsAccount("Asha", 1000)
s.deposit(500)
s.add_interest(10)      # 10% interest on 1500 is 150
print(s.get_balance())  # Output: 1650.0
s.withdraw(5000)        # Output: Not enough balance!

print("\n--- Current Account ---")
c = CurrentAccount("Bibek", 200, overdraft_limit=500)
c.withdraw(600)         # Allowed (goes to -400)
print(c.get_balance())  # Output: -400
c.withdraw(200)         # Output: Overdraft limit reached!
