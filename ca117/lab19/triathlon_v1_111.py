#!/usr/bin/env python3

''' modelling triathlon class '''

class Triathlete():

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        name = "Name: {:s}".format(self.name)
        tid = "ID: {:d}".format(self.tid)

        return "\n".join([name, tid])


class Triathlon(object):

    def __init__(self):
        self.athletes = {}

    def add(self, t):
        self.athletes[t.tid] = t

    # remove an athlete on the basis of their ID
    def remove(self, tid):
        self.athletes.pop(tid)

    def lookup(self, tid):
        if tid in self.athletes.keys():
            return self.athletes[tid]
