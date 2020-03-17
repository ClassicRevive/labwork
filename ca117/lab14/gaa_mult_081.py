#!/usr/bin/env python3

''' gaa score system (class) '''

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def score2points(self):
        return self.goals * 3 + self.points

    def __str__(self):
        return "{} goal(s) and {} point(s)".format(self.goals,
                                                   self.points)

    def __eq__(self, other):
        return self.score2points() == other.score2points()

    def __gt__(self, other):
        return other.score2points() < self.score2points()

    def __lt__(self, other):
        return self.score2points() < other.score2points()

    def __ge__(self, other):
        return other.score2points() <= self.score2points()

    def __le__(self, other):
        return self.score2points() <= other.score2points()

    def __add__(self, other):
        t = Score(self.goals + other.goals, self.points + other.points)
        return t

    def __sub__(self, other):
        t = Score(self.goals - other.goals, self.points - other.points)
        return t

    def __iadd__(self, other):
        t = self + other
        self.goals, self.points = t.goals, t.points
        return self

    def __isub__(self, other):
        t = self - other
        self.goals, self.points = t.goals, t.points
        return self

    def __mul__(self, multiple):
        t = Score(self.goals * multiple, self.points * multiple)
        return t

    def __rmul__(self, multiple):
        t = Score(self.goals * multiple, self.points * multiple)
        return t

    def __imul__(self, multiple):
        z = self * multiple
        self.goals, self.points = z.goals, z.points
        return self
