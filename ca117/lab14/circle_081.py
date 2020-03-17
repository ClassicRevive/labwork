#!/usr/bin/env python3

''' circles! '''

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def midpoint(self, other):
        midx, midy = ((self.x + other.x) / 2, (self.y + other.y) / 2)
        return Point(midx, midy)


class Circle(object):

    def __init__(self, centre=Point(), radius=1):
        self.centre = centre
        self.radius = radius

    def __str__(self):
        c = "({:.1f}, {:.1f})".format(self.centre.x, self.centre.y)
        return "Centre: {}\nRadius: {}".format(c, self.radius)

    def __add__(self, other):
        c = self.centre.midpoint(other.centre)
        r = self.radius + other.radius
        return Circle(c, r)


def main():
    p1 = Point()
    p2 = Point(4, 6)
    c1 = Circle(p1, 10)
    c2 = Circle(p2, 5)
    c3 = c1 + c2
    print(c3)

    p3 = Point(10, 10)
    c4 = Circle(p3, 15)
    c5 = c2 + c4
    print(c5)


if __name__ == '__main__':
    main()
