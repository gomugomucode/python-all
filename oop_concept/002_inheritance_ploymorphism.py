
# Base Class  (Bank class)

class Bank:
    def __init__(self, name, balance , account_number , bank_name, branch, ifsc_code):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.bank_name = bank_name
        self.branch = branch
        self.ifsc_code = ifsc_code

    # def display_info(self):
    #     print(f"Account Holder: {self.name}")
    #     print(f"Balance: {self.balance}")
    #     print(f"Account Number: {self.account_number}")
    #     print(f"Bank Name: {self.bank_name}")
    #     print(f"Branch: {self.branch}")
    #     print(f"IFSC Code: {self.ifsc_code}")

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

# Saving Account class inherits from Bank class by using Bank class as a parameter in the definition of SavingAccount class

class SavingAccount(Bank):
    def __init__(self, name, balance , account_number , bank_name, branch, ifsc_code, interest_rate):
        # calling bank class constructor to initilize the attributes of the Bank class

        super().__init__(name, balance , account_number , bank_name, branch, ifsc_code)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print(f"Interest for the current balance: {interest}")

    def withdraw(self, amount):
        if self.balance - amount < 1000:
            print(f"Cannot withdraw. Minimum balance of 1000 must be maintained.")
            print(f"Max you can withdraw: {self.balance - 1000}")
            return
            super().withdraw(amount)

    def __str__(self):
        return f"The account is created for {self.name} with account number {self.account_number} has a balance of {self.balance} in {self.bank_name} at {self.branch} branch with IFSC code {self.ifsc_code}."

class CurrentAccount(Bank):
    def __init__(self, name, balance , account_number , bank_name, branch, ifsc_code, overdraft_limit):
        super().__init__(name, balance , account_number , bank_name, branch, ifsc_code)
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
            super().withdraw(amount)  # Call the withdraw method of the Bank class
            print("This is a withdrawal from the Current Account.")

    def __str__(self):
        return f"The account is created for {self.name} with account number {self.account_number} has a balance of {self.balance} in {self.bank_name} at {self.branch} branch with IFSC code {self.ifsc_code} "

class FixedDepositAccount(Bank):
    def __init__(self, name, balance , account_number , bank_name, branch, ifsc_code, maturity_period , interest_rate):
        super().__init__(name, balance , account_number , bank_name, branch, ifsc_code)
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
        return f"The account is created for {self.name} with account number {self.account_number} has a balance of {self.balance} in {self.bank_name} at {self.branch} branch with IFSC code {self.ifsc_code} and a maturity period of {self.maturity_period} years with an interest rate of {self.interest_rate}%."



s1 = SavingAccount("Anupam", 5000, "1234567890", "ABC Bank", "Main ", "ABC0001234", 5)
print(s1)

s2 = CurrentAccount("John", 2000, "0987654321", "XYZ Bank", "City ", "XYZ0005678", 1000)
print(s2)   

s3 = FixedDepositAccount("Alice", 10000, "1122334455", "PQR Bank", "Town ", "PQR0009876", 3, 7)
print(s3)