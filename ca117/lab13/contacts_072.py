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

    def del_contact(self, name):
        if name in self.d:
            del self.d[name]

    # make a contact object from the name input
    def get_contact(self, name):
        if name in self.d:
            contact = Contact(name, self.d[name][0], self.d[name][1])  # name, phone, email
            return contact

    def __str__(self):
        person = []
        for k, v in self.d.items():
            contact = k + " " + v[0] + " " + v[1]
            person.append(contact)

        person.sort()
        string = "Contact list\n------------\n{}"\
                 .format("\n".join(person))

        return string
