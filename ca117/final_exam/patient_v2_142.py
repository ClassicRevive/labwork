#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor, meds):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.meds = meds

    def __str__(self):
        l = []
        l.append("Name: {:s}".format(self.name))
        l.append("Age: {:d}".format(self.age))
        l.append("Medications: {:s}".format(", ".join(self.meds)))
        l.append("Doctor: {:s}".format(self.doctor))

        return "\n".join(l)
