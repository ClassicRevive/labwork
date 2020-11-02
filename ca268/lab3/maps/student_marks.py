#!/user/bin/env python3

import sys

def make_map():
    students = {}

    for line in sys.stdin:
        if line.strip() != "":
            student, mark = line.rstrip().split()

            students[student] = mark

    return students
