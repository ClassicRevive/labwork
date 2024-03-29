#!/usr/bin/env python3

''' third version of triathlete class #!/usr/bin/env python3 '''

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

    def __eq__(self, other):
        return self.time == other.time

    def __gt__(self, other):
        return self.time > other.time

    def __lt__(self, other):
        return self.time < other.time

    def __str__(self):
        l = []
        l.append("Name: {:s}".format(self.name))
        l.append("ID: {:d}".format(self.tid))
        l.append("Race time: {}".format(self.time))
        return "\n".join(l)
