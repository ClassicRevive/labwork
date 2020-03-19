#!/usr/bin/env python3

class Time(object):

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __eq__(self, other):
        return ((self.hour, self.minute, self.second) ==
                (other.hour, other.minute, other.second))

    def __gt__(self, other):
        return self.time_to_seconds() > other.time_to_seconds()

    def __add__(self, other):
        return self.seconds_to_time(self.time_to_seconds() +
                                    other.time_to_seconds())

    def __iadd__(self, other):
        z = self + other  # calls the __add__ special function
        self.hour, self.minute, self.second = z.hour, z.minute, z.second

        return self

    def __str__(self):
        return 'The time is {:02d}:{:02d}:{:02d}'.format(self.hour,
                                                         self.minute,
                                                         self.second)

    def time_to_seconds(self):
        return self.hour * 60 * 60 + self.minute * 60 + self.second

    @classmethod
    def seconds_to_time(cls, s):
        minute, second = divmod(s, 60)
        hour, minute = divmod(minute, 60)
        overflow, hour = divmod(hour, 24)

        return cls(hour, minute, second)


def main():
    t1 = Time.seconds_to_time(233700)
    t2 = Time.seconds_to_time(120)
    print("t1: {}\nt2: {}".format(t1, t2))
    print(t1 > t2)


if __name__ == '__main__':
    main()
