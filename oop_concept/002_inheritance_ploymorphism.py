class Bank:
    def __init__(self, name, balance, account_number, bank_name, branch, ifsc_code):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.bank_name = bank_name
        self.branch = branch
        self.ifsc_code = ifsc_code

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def __str__(self):
        return f"The bank account of {self.name} with account number {self.account_number} has a balance of {self.balance} in {self.bank_name} at {self.branch} branch with IFSC code {self.ifsc_code}."


class SavingAccount(Bank):
    def __init__(self, name, balance, account_number, bank_name, branch, ifsc_code, interest_rate):
        super().__init__(name, balance, account_number, bank_name, branch, ifsc_code)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print(f"Interest for the current balance: {interest}")

    def withdraw(self, amount):
        # Fixed Logic: Only call super if the check passes
        if self.balance - amount < 1000:
            print(f"Cannot withdraw. Minimum balance of 1000 must be maintained.")
            print(f"Max you can withdraw: {self.balance - 1000}")
            return
        
        super().withdraw(amount)

    def __str__(self):
        return f"The Saving Account of {self.name} (Acc: {self.account_number}) has a balance of {self.balance} in {self.bank_name}. Interest Rate: {self.interest_rate}%."


class CurrentAccount(Bank):
    def __init__(self, name, balance, account_number, bank_name, branch, ifsc_code, overdraft_limit):
        super().__init__(name, balance, account_number, bank_name, branch, ifsc_code)
        self.overdraft_limit = overdraft_limit

    def check_overdraft(self):
        if self.balance < 0:
            print(f"Overdraft limit exceeded. Current overdraft: {-self.balance}")
        else:
            print("No overdraft. Current balance is sufficient.")

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            print("Overdraft limit exceeded. Cannot withdraw.")
        else:
            super().withdraw(amount)
            print("This is a withdrawal from the Current Account.")

    def __str__(self):
        return f"The Current Account of {self.name} (Acc: {self.account_number}) has a balance of {self.balance} in {self.bank_name}. Overdraft Limit: {self.overdraft_limit}."


class FixedDepositAccount(Bank):
    def __init__(self, name, balance, account_number, bank_name, branch, ifsc_code, maturity_period, interest_rate):
        super().__init__(name, balance, account_number, bank_name, branch, ifsc_code)
        self.maturity_period = maturity_period
        self.interest_rate = interest_rate

    def check_maturity(self):
        print(f"Maturity period for this account is {self.maturity_period} years.")

    def withdraw(self, amount):
        print("Withdrawals are not allowed from a Fixed Deposit Account until maturity.")

    def calculate_maturity_amount(self):
        maturity_amount = self.balance * (1 + (self.interest_rate / 100)) ** self.maturity_period
        print(f"Maturity amount after {self.maturity_period} years: {maturity_amount}")

    def __str__(self):
        return f"The Fixed Deposit Account of {self.name} (Acc: {self.account_number}) has a deposit of {self.balance} in {self.bank_name}. Maturity: {self.maturity_period} yrs, Rate: {self.interest_rate}%."


# Test Instances
s1 = SavingAccount("Anupam", 5000, "1234567890", "ABC Bank", "Main", "ABC0001234", 5)
print(s1)
s1.withdraw(4500) # Should fail (balance < 1000)
s1.withdraw(3000) # Should succeed

print("\n" + "-"*30 + "\n")

s2 = CurrentAccount("John", 2000, "0987654321", "XYZ Bank", "City", "XYZ0005678", 1000)
print(s2)
s2.withdraw(2500) # Should succeed (uses overdraft)
s2.check_overdraft()

print("\n" + "-"*30 + "\n")

s3 = FixedDepositAccount("Alice", 10000, "1122334455", "PQR Bank", "Town", "PQR0009876", 3, 7)
print(s3)
s3.withdraw(5000) # Should print "Withdrawals not allowed"
s3.calculate_maturity_amount()