#!/usr/bin/env python3

# one gaa goal is 3 points
# score class has goals and points in that order in init function

class Score():

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points
        self.total = 3 * goals + points

    def less_than(self, other):
        return self.total < other.total

    def greater_than(self, other):
        return other.total < self.total

    def equal_to(self, other):
        return self.total == other.total

def main():

    score1 = Score()
    score2 = Score(3, 9)
    score3 = Score(4, 6)

    print(score1.less_than(score2))
    print(score3.less_than(score1))
    print(score1.greater_than(score2))
    print(score3.greater_than(score2))
    print(score1.greater_than(score1))
    print(score2.greater_than(score1))
    print(score2.equal_to(score1))
    print(score3.equal_to(score2))

if __name__ == '__main__':
    main()
