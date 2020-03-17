#!/usr/bin/env python3

''' develope a coin class for probability sampling '''
import random

class Coin():

    def __init__(self, sideup="Heads"):
        self.sideup = sideup

    def __str__(self):
        return("Current state : {}".format(self.sideup))

    def flip(self):
        self.sideup = random.choice(["Heads", "Tails"])

    def getstate(self):
        return self.sideup


def main():
    c = Coin()
    for i in range(10):
        c.flip()
        print(c)

    # 1000 coin flip scenarios, count double heads occurences
    total = 0
    p_state = c.sideup;
    for i in range(1000):
        c.flip()
        if p_state == c.sideup == 'Heads':
            total += 1
        p_state = c.sideup

    print('The odds of two heads in a row is: {:.2f}'.format(total/1000))

if __name__ == '__main__':
    main()
