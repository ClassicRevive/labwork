#!/usr/bin/env python3

from math import sqrt

class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Shape():

    def __init__(self, points):
        self.points = points

    # returns list of lengths of shape side
    # p1-p2, p2-p3, ..., pn-p1
    def sides(self):
        sides = []

        i = 0
        while i < len(self.points) - 1:
            sides.append(self.points[i].distance(self.points[i + 1]))

            i += 1

        sides.append(self.points[i].distance(self.points[0]))
        return sides

    def perimeter(self):
        return sum(self.sides())


class Triangle(Shape):

    def area(self):
        [a, b, c] = self.sides()
        s = (a + b + c) / 2
        heron_area = sqrt(s * (s - a) * (s - b) * (s - c))

        return heron_area


class Square(Shape):

    def area(self):
        side = self.sides()[0]
        return side * side
