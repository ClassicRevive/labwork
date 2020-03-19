#!/usr/bin/env python3

class BankAccount(object):
    # define class variables
    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, forename, surname, balance=0, account_number=next_account_number):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def lodge(self, amount):
        self.balance += amount
        BankAccount.total_lodgements += 1

    def apply_interest(self):
        self.balance *= (1 + BankAccount.interest_rate)

    def __iadd__(self, other):
        if type(other) is int:
            self.lodge(other)
        else:
            self.lodge(other.balance)

        return self

    def __str__(self):
        name = "Name: {} {}".format(self.forename, self.surname)
        account = "Account number: {}".format(self.account_number)
        balance = "Balance: {:.2f}".format(self.balance)
        return "\n".join([name, account, balance])
