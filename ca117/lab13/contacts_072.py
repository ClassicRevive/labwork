#!/usr/bin/env python3

''' make contacts class '''

class Contact():

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


    def __str__(self):
        return "{} {} {}".format(self.name, self.phone, self.email)


class ContactList():

    # define empty contact list at initialisation
    def __init__(self):
        self.d = {}

    # add contact to list
    def add_contact(self, contact):
        self.d[contact.name] = contact.phone, contact.email
        # print(self.d)
    def del_contact(self, name):
        if name in self.d:
            del self.d[name]

    # make a contact object from the name input
    def get_contact(self, name):
        if name in self.d:
            print(self.d[name][0])
            c = Contact(name, self.d[name][0], self.d[name[1]])  # name, phone, email
            return c

    def __str__(self):
        pass

import sys
def main():
    pass
