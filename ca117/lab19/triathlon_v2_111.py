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

    def get_name(self, t):
        t = self.lookup(t[0])  # find athletes name and use for sorting(above)
        return t.name

    def __str__(self):
        l = []
        # add the string forms of each of the athletes in the dictionary
        # to a list which will be concatenated as the triathlon string form
        for athlete in sorted(self.athletes.items(), key=self.get_name):
            l.append(Triathlete.__str__(self.lookup(athlete[0])))

        # print(l)
        return "\n".join(l)
