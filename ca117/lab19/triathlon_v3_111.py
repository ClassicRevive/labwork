#!/usr/bin/env python3

''' modelling triathlon class '''


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

    def rtime(self, t):
        return t[1]

    def best(self):
        times = {}
        for n in self.athletes:
            athlete = self.lookup(n)
            times[athlete.tid] = athlete.race_time

        # get the id of athlete with the smallest race time and
        # return their string form
        best = min(times.items(), key=self.rtime)[0]
        return Triathlete.__str__(self.lookup(best))

    def worst(self):
        times = {}
        for n in self.athletes:
            athlete = self.lookup(n)
            times[athlete.tid] = athlete.race_time

        # get the id of athlete with the smallest race time and
        # return their string form
        worst = max(times.items(), key=self.rtime)[0]
        return Triathlete.__str__(self.lookup(worst))

    def __str__(self):
        l = []
        # add the string forms of each of the athletes in the dictionary
        # to a list which will be concatenated as the triathlon string form
        for athlete in sorted(self.athletes.items(), key=self.get_name):
            l.append(Triathlete.__str__(self.lookup(athlete[0])))

        return "\n".join(l)
