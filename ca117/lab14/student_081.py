#!/usr/bin/env python3

from collections import namedtuple

Module = namedtuple('Module', 'code title ects')

CA1_MODULES = {'CA103': Module('CA103', 'Computer Systems', 5),
               'CA106': Module('CA106', 'Web Design', 5),
               'CA115': Module('CA115', 'Digital Innovation', 5),
               'CA116': Module('CA116', 'Computer Programming I', 10),
               'CA117': Module('CA117', 'Computer Programming II', 10),
               'CA169': Module('CA169', 'Networks and Internet', 5),
               'CA170': Module('CA170', 'Operating Systems', 5),
               'CA172': Module('CA172', 'Problem Solving', 5),
               'MS121': Module('MS121', 'IT Mathematics', 10)}

class Student(object):
    def __init__(self, idnum, surname, firstname):
        self.idnum = idnum
        self.surname = surname
        self.firstname = firstname
        self.mods = CA1_MODULES
        self.marks = {code: 0 for code in self.mods.keys()}
        self.tc = 0
        for m in self.mods:
            self.tc += self.mods[m].ects

    def __str__(self):  # table format for student data
        name = '{} : {} {}'.format(self.idnum,
                                   self.firstname,
                                   self.surname)
        uline = '-' * len(name)
        results = '\n'.join(
            [code + ' : ' + self.mods[code].title + ' : ' + str(
                self.marks[code]) for code in sorted(self.mods.keys())])

        pm = 'Precision mark: {:.2f}'.format(self.precision_mark())
        if self.passed():
            outcome = 'Pass'
        elif self.passed_by_compensation():
            outcome = 'Pass by compensation'
        else:
            outcome = 'Fail'

        return '\n'.join([name, uline, results, pm, outcome])

    def add_mark(self, code, mark):
        # update the mark in the marks dictionary

        self.marks[code] = mark

    def precision_mark(self):
        # add the weighted average of the mark in that module
        # to the avg total
        avg = 0
        for module in self.mods:
            weighted_mark = self.marks[module] * (self.mods[module].ects / self.tc)
            avg += weighted_mark

        return avg

    def passed(self):
        passed = True
        for code, marks in self.marks.items():
            if marks < 40:
                passed = False

        return passed

    def passed_by_compensation(self):
        # calculate how much credits are recieved based on pass or fail

        mincreds = self.tc - ((1 / 6) * self.tc)
        credits = 0
        for code, marks in self.marks.items():
            if 39 < marks:
                credits += self.mods[code].ects

        # linear search for any marks below 35
        over35 = True
        for code, marks in self.marks.items():
            if marks < 35:
                over35 = False
                break

        return 44 < self.precision_mark() and mincreds <= credits and over35
