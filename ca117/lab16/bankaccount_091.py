#!/usr/bin/env python3

class BankAccount():
    next_account_number = 16555232
    account_type = "General"

    def __init__(self, forename, surname, balance=0):
        self.forename = forename
        self.surname = surname
        self._balance = balance
        self.account_number = self.next_account_number

        BankAccount.next_account_number += 1

    def lodge(self, amount):
        self._balance += amount

        return self

    def withdraw(self, amount):
        if self._balance < amount:
            print("Insufficient funds available")
        else:
            self._balance -= amount
            return self

    def __str__(self):
        l = []
        l.append("Name: {} {}".format(self.forename, self.surname))
        l.append("Account number: {}".format(self.account_number))
        l.append("Account type: {}".format(self.account_type))
        l.append("Balance: {:.2f}".format(self._balance))

        return "\n".join(l)

class CurrentAccount(BankAccount):
    overdraft = -1000

    def withdraw(self, amount):
        if amount <= self._balance - self.overdraft:
            self._balance -= amount
        else:
            print("Insufficient funds available")

    def __str__(self):
        l = []
        l.append(super().__str__())
        l.append("Overdraft: {:.2f}".format(self.overdraft))

        return "\n".join(l)


class SavingsAccount(BankAccount):
    interest_rate = 0.01
    account_type = "Savings"

    def apply_interest(self):
        self._balance *= (1 + self.interest_rate)

        return self

    def __str__(self):
        l = []
        l.append(super().__str__())
        l.append("Interest rate: {}".format(self.interest_rate))

        return "\n".join(l)
