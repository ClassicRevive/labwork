#!/usr/bin/env python3

''' determine day of the week that child is born based on date cmd arguements'''

import sys
import calendar

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
poem = ["Monday's child is fair of face.",
        "Tuesday's child is full of grace.",
        "Wednesday's child is full of woe.",
        "Thursday's child has far to go.",
        "Friday's child is loving and giving.",
        "Saturday's child works hard for a living.",
        "Sunday's child is fair and wise and good in every way."]

def main():
    date = sys.argv[1:]

    for i in range(len(date)):
        date[i] = int(date[i])

    [y, m, d] = date
    day = calendar.weekday(d, m, y)
    print("You were born on a {} and {}".format(days[day], poem[day]))

if __name__ == '__main__':
    main()
