from abc import ABC, abstractmethod
from datetime import datetime


class Bank(ABC):
    def __init__(
        self, name, balance, account_number, bank_name, branch, ifsc_code, **kwargs
    ):
        super().__init__(**kwargs)
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.bank_name = bank_name
        self.branch = branch
        self.ifsc_code = ifsc_code

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")


class LogMixin:
    def __init__(self, logs=None, **kwargs):
        super().__init__(**kwargs)
        self.logs = logs if logs is not None else []

    # hasattr() is used to check if the object have a variable name or not. Syntax hasattr(object , variable_name) it will return true if the variable is present in the object otherwise it will return false
    def log_message(self, message):
        # if not hasattr(self, 'logs'):
        #     self.logs = []
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.append(f"[{timestamp}] {message}")
        # print(f"[LOG] {message}")

    def show_logs(self):
        if not hasattr(self, "logs"):
            print("No logs available.")
            return
            # in get attr it get value from variable  name and if not found it give us the default value   syntax getattr(object, variable_name , default_value)
        print(f"log for {getattr(self , 'name' , 'Account')}:")
        for log in self.logs:
            print(log)


class NotificationMixin:
    def send_notification(self, message):
        print(f"[NOTIFICATION → {getattr(self, 'name', 'Account')}]: {message}")


class SavingAccount(Bank, LogMixin, NotificationMixin):
    def __init__(
        self,
        name,
        balance,
        account_number,
        bank_name,
        branch,
        ifsc_code,
        interest_rate,
        logs=None,
    ):
        super().__init__(
            name=name,
            balance=balance,
            account_number=account_number,
            bank_name=bank_name,
            branch=branch,
            ifsc_code=ifsc_code,
            logs=logs,
        )
        self.interest_rate = interest_rate

    def deposit(self, amount):
        super().deposit(amount)
        self.log_message(f"Deposited {amount}. New Balance: {self.balance}")
        self.send_notification(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            self.log_message("Insufficient balance.")
            return
        self.balance -= amount
        self.log_message(f"Withdrew {amount}. New balance: {self.balance}")
        self.send_notification(f"Withdrew {amount}. New balance: {self.balance}")

    def account_type(self):
        return "Savings Account"


class CurrentAccount(Bank, LogMixin, NotificationMixin):
    def __init__(
        self,
        name,
        balance,
        account_number,
        bank_name,
        branch,
        ifsc_code,
        overdraft_limit=0,
        logs=None,
    ):
        super().__init__(
            name=name,
            balance=balance,
            account_number=account_number,
            bank_name=bank_name,
            branch=branch,
            ifsc_code=ifsc_code,
            logs=logs,
        )
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        super().deposit(amount)
        self.log_message(f"Deposited {amount}. New Balance: {self.balance}")
        self.send_notification(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount < self.overdraft_limit:
            msg = "Overdraft limit exceeded. Cannot withdraw."
            self.log_message(msg)
            self.send_notification(msg)
            return
        self.balance -= amount
        msg = f"Withdrew {amount}. New balance: {self.balance}"
        self.log_message(msg)
        self.send_notification(msg)

    def account_type(self):
        return "Current Account"


class FixedDepositAccount(Bank):
    def __init__(
        self,
        name,
        balance,
        account_number,
        bank_name,
        branch,
        ifsc_code,
        maturity_period,
        interest_rate,
    ):
        super().__init__(
            name=name,
            balance=balance,
            account_number=account_number,
            bank_name=bank_name,
            branch=branch,
            ifsc_code=ifsc_code,
        )
        self.maturity_period = maturity_period
        self.interest_rate = interest_rate

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount):
        print(
            "Withdrawals are not allowed from a fixed deposit account until maturity."
        )

    def account_type(self):
        return "Fixed Deposit Account"


if __name__ == "__main__":

    saving_acc = SavingAccount(
        "Alice", 1000, "1234567890", "Bank of Python", "Main Branch", "PYTH0001", 0.05
    )
    current_acc = CurrentAccount(
        "Bob", 5000, "0987654321", "Bank of Python", "Main Branch", "PYTH0001"
    )

    saving_acc.deposit(500)
    saving_acc.withdraw(200)
    saving_acc.log_message("Performed a withdrawal of 200.")
    (saving_acc.show_logs())
    print("\n")

    current_acc.deposit(1000)
    current_acc.withdraw(300)
    current_acc.log_message("Attempted a withdrawal of 300.")
    (current_acc.show_logs())
    print("\n")

    try:
        bad = Bank("Test", 1000, "000", "X", "Y", "Z")  # should crash
    except TypeError as e:
        print(f"✓ ABC works: {e}")

    # Also prove account_type() works polymorphically
    accounts = [saving_acc, current_acc]
    for acc in accounts:
        print(f"{acc.name} → {acc.account_type()}")
