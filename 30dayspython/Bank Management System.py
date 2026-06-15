class BankAccount:
    def __init__(self, name, __balance):

        self.name = name
        self.__balance = __balance

    @property
    def get_balance(self):
        return self.__balance

    @get_balance.setter
    def get_balance(self, new_balance):
        if isinstance(new_balance, (int, float)):
            raise ValueError("Balance must be a number")
        self.__balance = new_balance

    def deposit(self, amount):
        if isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")

        if amount < 0:
            raise ValueError("Amount must be a greater than zero ")

        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")

        if amount < 0 or self.__balance < 0:
            raise ValueError(
                "Withdraw Amount must be a greater than zero  or balance is insufficient"
            )

        self.__balance -= amount
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, name, __balance, interest):
        super().__init__(name, __balance)
        self.interest = interest

    def add_interest(self, rate):
        self.interest = (self.__balance * rate) / 100
        return self.interest

    def deposit(self, amount):
        return super().deposit(amount)

    @property
    def get_balance(self):
        return super().get_balance

    @get_balance.setter
    def get_balance(self):
        self.__balance += self.interest

    def withdraw(self, amount):
        return super().withdraw(amount)

class CurrentAccount(BankAccount):
    def __init__(self, name, __balance , overdraft_limit):
        super().__init__(name, __balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        return super().deposit(amount)
    
    def withdraw(self, amount):
        if isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")

        if amount < 0 or amount > (self.__balance + self.overdraft_limit):
            raise ValueError("Amount must be a number or amount is overdraft")
        
        if self.__balance < amount:

            if amount < (self.__balance + self.overdraft_limit):
                self.__balance = self.__balance + self.overdraft_limit - amount
                return self.__balance

        
#  Savings account
s = SavingsAccount("Asha", 1000)
s.deposit(500)
s.add_interest(10) # 10% interest
print(s.get_balance()) # 1650.0
s.withdraw(5000) # Not enough balance!

# Current account with overdraft
c = CurrentAccount("Bibek", 200, overdraft_limit=500)
c.withdraw(600) # allowed (goes to -400)
print(c.get_balance()) # -400
c.withdraw(200) # Overdraft limit reached!