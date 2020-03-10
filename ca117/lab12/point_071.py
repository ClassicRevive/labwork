
class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect(self):
        self.x = -self.x
        self.y = -self.y

    def distance(self, other):
        x1, y1, x2, y2 = (self.x, self.y, other.x, other.y)
        distance = (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2))

        return distance
