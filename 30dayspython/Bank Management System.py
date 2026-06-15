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

    def withdraw(self, amount):
        if isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")

        if amount < 0 or self.__balance < 0:
            raise ValueError(
                "Withdraw Amount must be a greater than zero  or balance is insufficient"
            )

        self.__balance -= amount
