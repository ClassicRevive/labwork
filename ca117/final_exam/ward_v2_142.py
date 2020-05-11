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


class Ward(object):

    def __init__(self):
        self.d = {}

    # add patient objects to the dictionary with key = name
    def add(self, patient):
        self.d[patient.name] = patient

    def remove(self, name):
        del self.d[name]

    def lookup(self, name):
        if name in self.d:
            return self.d[name]

    def get_patients_by_medication(self, medication):
        patients = []
        for k, v in self.d.items():
            if medication in v.meds:
                patients.append(v)

        return patients
