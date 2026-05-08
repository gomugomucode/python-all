
# # ?creating class
# class Student:
#     name = "Anupam"
    
# # ?creating object
# s1 = Student()
# # print(s1.name)
# print(f"My name is {s1.name}")


# class Car:
#     name= "BMW"
# c1 = Car()
# print(f"My car name is {c1.name}")



# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # Creating objects of the Student class
# s1 = Student("Anupam", 20)
# s2 = Student("John", 22)

# # Accessing the attributes of the objects
# print(f"Student 1: {s1.name}, Age: {s1.age}")
# print(f"Student 2: {s2.name}, Age: {s2.age}")

import random

class Bank:
    def __init__(self, name, balance , account_number , bank_name, branch, ifsc_code ,   ):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.bank_name = bank_name
        self.branch = branch
        self.ifsc_code = ifsc_code

    def display_info(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")
        print(f"Account Number: {self.account_number}")
        print(f"Bank Name: {self.bank_name}")
        print(f"Branch: {self.branch}")
        print(f"IFSC Code: {self.ifsc_code}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")

n = int(input("Enter the number of accounts you want to create: "))
while n > 0:
    name = input("Enter account holder's name: ")
    balance = float(input("Enter initial balance: "))
    account_number = random.randint(1000000000, 9999999999)  # Generating a random 10-digit account number
    bank_name = input("Enter bank name: ")
    branch = input("Enter branch: ")
    ifsc_code = input("Enter IFSC code: ")

    # Creating an object of the Bank class
    account = Bank(name, balance, account_number, bank_name, branch, ifsc_code)
    
    # Displaying account information
    account.display_info()
     
    # Example of deposit and withdrawal
    deposit_amount = float(input("Enter amount to deposit: "))
    account.deposit(deposit_amount)

    withdraw_amount = float(input("Enter amount to withdraw: "))
    if withdraw_amount > account.balance or withdraw_amount <= 100:
        print("Insufficient funds for withdrawal or withdrawal amount is too low.")
    else:
        account.withdraw(withdraw_amount)

    n -= 1

 

    