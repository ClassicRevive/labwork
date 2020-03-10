#!/usr/bin/env python3

''' modelling student class '''

class Student():

    def __init__(self, surname, forename, sid, modlist=None):
        self.sid = sid
        self.surname = surname
        self.forename = forename

        if modlist is None:
            self.modlist = []
        else:
            self.modlist = modlist

    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)

    def print_details(self):
        print("ID: {}\nSurname: {}\nForename: {}\nModules: {}"
              .format(self.sid, self.surname, self.forename, " ".join(self.modlist)))
