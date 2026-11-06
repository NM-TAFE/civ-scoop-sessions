"""
# Class level
## Attr
Bank name


# Object

## Attributes
- account name
- bsb
- account number
- balance

## Methods
check_balance()
send_money()
    * amount
    * // channel (bpay, direct debit, osko)
receive_money()
    * amount
"""

# Task 1: Implement toy BankAccount class using the above
# Task 2: Create (in a main.py file) at least 2 bank accounts
# and have them pay each other $50

class BankAccount:
    def __init__(
            self,
            account_name,
            bsb,
            account_number,
            opening_balance
        ):
        self.__account_name = account_name
        self.__bsb = bsb
        self.__account_number = account_number
        self.__balance = opening_balance

    # This "getter" pattern is "un-Pythonic", but is seen in many other languages
    # We'll learn @property soon
    def get_account_name(self):
        return self.__account_name

    def get_bsb(self):
        return self.__bsb

    def get_account_number(self):
        return self.__account_number

    def check_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.__account_name}: {self.__bsb}-{self.__account_number}. ${self.__balance}"

    def set_account_name(self, new_name):
        if len(new_name) < 1:
            raise ValueError("Name must be at least 1 letter long")
        self.__account_name = new_name

    def send_money(self, amount, receiver):
        if self.__balance < amount:
            raise ValueError("Cannot overdraw account")

        if not isinstance(receiver, BankAccount):
            raise ValueError("Receiver must be a BankAccount")

        self.__balance -= amount
        receiver.receive_money(amount) # Weird and mysterious

    def receive_money(self, amount):
        self.__balance += amount