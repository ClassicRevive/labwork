#!/usr/bin/env python3

class Triathlete():

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.d = {}
        self.time = 0

    def add_time(self, sport, t):
        self.d[sport] = t
        self.time += t

    def get_time(self, sport):
        return self.d[sport]

    def __str__(self):
        l = []
        l.append("Name: {:s}".format(self.name))
        l.append("ID: {:d}".format(self.tid))
        l.append("Race time: {}".format(self.time))
        return "\n".join(l)

class Triathlon(object):

    def __init__(self):
        self.d = {}

    def add(self, athlete):
        self.d[athlete.tid] = athlete

    def remove(self, tid):
        del self.d[tid]

    def lookup(self, tid):
        if tid in self.d.keys():
            return self.d[tid]
