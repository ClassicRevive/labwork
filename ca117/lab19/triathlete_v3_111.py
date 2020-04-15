#!/usr/bin/env python3

''' modelling a triathlete class '''

class Triathlete():

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}
        self.race_time = 0

    def add_time(self, sport, time):
        self.times[sport] = time
        self.race_time += time

    def get_time(self, sport):
        if sport in self.times:
            return self.times[sport]

    def __eq__(self, other):
        return self.race_time == other.race_time

    def __lt__(self, other):
        return self.race_time < other.race_time

    def __gt__(self, other):
        return self.race_time > other.race_time

    def __str__(self):
        name = "Name: {:s}".format(self.name)
        tid = "ID: {:d}".format(self.tid)
        time = "Race time: {}".format(self.race_time)

        return "\n".join([name, tid, time])
