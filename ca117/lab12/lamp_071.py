#!/usr/bin/env python3

''' class for lamp data type '''
class Lamp():

    def __init__(self, on=False):
        self.on = on

    def on(self):
        print(self.on)

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def toggle(self):
        self.on = not(self.on)
