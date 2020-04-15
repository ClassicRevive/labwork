#!/usr/bin/env python3

''' modelling a triathlete class '''

class Triathlete():

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        name = "Name: {:s}".format(self.name)
        tid = "ID: {:d}".format(self.tid)

        return "\n".join([name, tid])


def main():
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)

    assert(t1.name == 'Ian Brown')
    assert(t1.tid == 21)

    print(t1)
    print(t2)

if __name__ == '__main__':
    main()
