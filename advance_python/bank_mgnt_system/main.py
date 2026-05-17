
import sqlite3
import random

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder 
        
        # 1. Connect to the vault
        conn = sqlite3.connect("bank_mgmt_system.db")
        cursor = conn.cursor()

        # 2. Check if the user already exists
        # We use a parameterized query (?) to safely check the name
        cursor.execute("SELECT account_number, balance FROM user WHERE name = ?", (self.account_holder,))
        
        # fetchone() gets the first row found, or returns None if nothing is found
        existing_user = cursor.fetchone() 

        if existing_user is None:
            # 3A. THE USER IS NEW (Sign Up)
            self.account_number = random.randint(100000, 999999)
            self.balance = initial_balance
            
            sql_insert = "INSERT INTO user (name, account_number, balance) VALUES (?, ?, ?)"
            cursor.execute(sql_insert, (self.account_holder, self.account_number, self.balance))
            conn.commit()
            print(f"New Account Created! Account #: {self.account_number}")
            
        else:
            # 3B. THE USER ALREADY EXISTS (Log In)
            # existing_user is a tuple matching our SELECT: (account_number, balance)
            self.account_number = existing_user[0] 
            self.balance = existing_user[1]
            print(f"Welcome back, {self.account_holder}! Account loaded. Account Number is #{self.account_number}")

        # 4. Close the vault
        conn.close()

    def __str__(self):
        return f"\n Account belonging to {self.account_holder}.\n Current balance: ${self.balance}"

    def _update_db_balance(self):
        """Internal helper method to sync the current balance to the database."""
        conn = sqlite3.connect("bank_mgmt_system.db")
        cursor = conn.cursor()
        sql_update = "UPDATE user SET balance = ? WHERE account_number = ?"
        cursor.execute(sql_update, (self.balance, self.account_number))
        conn.commit()
        conn.close()

    def deposit(self, amount):
        # GUARD CLAUSE: If the amount is bad, stop everything and raise an error.
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
       
        
        # If the code reaches this line, the amount MUST be valid. No 'else' needed.

        self.balance += amount
        self._update_db_balance()
        
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        # GUARD CLAUSE 1: Check for negative/zero amounts
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        
        # GUARD CLAUSE 2: Check for insufficient funds
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal.")
            
        # If it survives both guard clauses, do the math.

        self.balance -= amount
        self._update_db_balance()
        
        return f"Withdrew ${amount}. New balance: ${self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0, interest_rate=0.05):
            # 1. Command the parent class to do the heavy lifting (DB connection, generate account #)
        super().__init__(account_holder, initial_balance)
            
            # 2. Add the child's unique attributes
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned
        self._update_db_balance()
        return(f"Interest applied! Earned ${interest_earned}. New balance: ${self.balance}")

    def __str__(self):
        return f"\n SAVINGS Account belonging to {self.account_holder}.\n Current balance: ${self.balance}"

    # 2. Overriding the withdraw method
    def withdraw(self, amount):
        # NEW SAVINGS BOUNCER: Check the $100 minimum balance rule
        if (self.balance - amount) < 100:
            raise ValueError("Savings accounts must maintain a $100 minimum balance.")
        
        # If the bouncer lets them pass, DO NOT rewrite the math and database code.
        # Just command the parent class to run its own withdraw method!
        return super().withdraw(amount)



# my_account = BankAccount("Anupam", 5000)


# print(my_account.deposit(1000))
# print(my_account)

# 1. Create the new Savings Account
my_savings = SavingsAccount("Anupam", 1000, 0.05) # 5% interest rate

# 2. Test inherited methods (these should work automatically!)
# print(my_savings.deposit(500))


print("\n--- ATTEMPTING $9000 WITHDRAWAL ---")
try:
    # We TRY to do the dangerous thing
    print(my_savings.withdraw(9000))
    
except ValueError as e:
    # If the class throws a bomb (ValueError), we CATCH it here (as 'e') 
    # and print a nice message instead of crashing the program!
    print(f"🚨 TRANSACTION DECLINED: {e}")



# 3. Test the child's unique method
print(my_savings.apply_interest())

# 4. Print the account

print("\n--- FINAL ACCOUNT STATUS ---")
print(my_savings)