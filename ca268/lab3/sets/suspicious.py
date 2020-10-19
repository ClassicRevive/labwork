#!/usr/bin/env python3

# check students file for names that are in delinquents list.
# ie. cross check both files using sets

import sys
my_students, the_delinuents = sys.argv[1:]

with open(my_students, "r") as f1:
    students = f1.readlines()
    for i in range(len(students)):
        students[i] = students[i].rstrip()
    students = set(students)

    with open(the_delinuents, "r") as f2:
        delinquents = f2.readlines()
        for i in range(len(delinquents)):
            delinquents[i] = delinquents[i].rstrip()

        delinquents = set(delinquents)
    
    matches = sorted(list(students.intersection(delinquents)))

for i in range(len(matches)):
    print("{}. {}".format(i + 1, matches[i]))
