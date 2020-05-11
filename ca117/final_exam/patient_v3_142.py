#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor, meds=None):
        self.name = name
        self.age = age
        self.doctor = doctor

        # if no meds are addeed in initialization
        # then meds is an empty list
        if meds is None:
            self.meds = []
        else:
            self.meds = meds

    def add_medication(self, s):
        self.meds.append(s)

    def __str__(self):
        l = []
        l.append("Name: {:s}".format(self.name))
        l.append("Age: {:d}".format(self.age))
        l.append("Medications: {:s}".format(", ".join(self.meds)))
        l.append("Doctor: {:s}".format(self.doctor))

        return "\n".join(l)
