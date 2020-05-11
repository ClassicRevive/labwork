#!/usr/bin/env python3

class Triathlete():

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.time = 0

    def __str__(self):
        l = []
        l.append("Name: {:s}".format(self.name))
        l.append("ID: {:d}".format(self.tid))
        return "\n".join(l)
