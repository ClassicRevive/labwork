#!/usr/bin/env python3

class Triathlete():

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.d = {}
        self.time = 0

    def __str__(self):
        l = []
        l.append("Name: {:s}".format(self.name))
        l.append("ID: {:d}".format(self.tid))
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

    def sort(self, t):
        return t[1].name

    def __str__(self):
        l = []
        for k, v in sorted(self.d.items(), key=self.sort):
            l.append(Triathlete.__str__(v))

        return "\n".join(l)
