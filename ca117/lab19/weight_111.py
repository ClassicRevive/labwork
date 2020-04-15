#!/usr/bin/env python3

''' modelling weight class '''

class Weight(object):
    OUNCES_PER_POUND = 16

    def __init__(self, pounds=0, ounces=0):
        self.pounds = pounds
        self.ounces = ounces

    # total weight for comparisons
    def total_weight(self):
        return Weight.OUNCES_PER_POUND * self.pounds + self.ounces

    def __str__(self):
        return "{:d} pound(s) and {:d} ounce(s)".format(self.pounds, self.ounces)

    def __ne__(self, other):
        return self.total_weight() != other.total_weight()

    def __eq__(self, other):
        return self.total_weight() == other.total_weight()

    def __lt__(self, other):
        return self.total_weight() < other.total_weight()

    def __gt__(self, other):
        return self.total_weight() > other.total_weight()

    def __le__(self, other):
        return self.total_weight() <= other.total_weight()

    def __ge__(self, other):
        return self.total_weight() >= other.total_weight()

    def __iadd__(self, other):
        z = self + other
        self.pounds, self.ounces = z.pounds, z.ounces
        return self

    def __mul__(self, x):
        return self.from_ounces(self.total_weight() * x)

    @classmethod
    def from_ounces(cls, n):
        pounds, ounces = divmod(n, 16)
        return cls(pounds, ounces)

    def __add__(self, other):
        return self.from_ounces(self.total_weight() + other.total_weight())
