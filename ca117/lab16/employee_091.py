#!/usr/bin/env python3

class Employee():
    salary = 0

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def wages(self):
        return self.salary

    def __str__(self):
        l = []
        l.append("Name: {:s}".format(self.name))
        l.append("Number: {:d}".format(self.number))
        l.append("Wages: {:.2f}".format(self.wages()))

        return "\n".join(l)


class Manager(Employee):

    def __init__(self, name, number, salary):
        super().__init__(name, number)
        self.salary = salary

    def wages(self):
        return self.salary / 52


class AssemblyWorker(Employee):

    def __init__(self, name, number, hourly_rate=0, hours=0):
        super().__init__(name, number)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def wages(self):
        return self.hourly_rate * self.hours


def test():

    e1 = Manager('Mary', 1, 50000)
    e2 = AssemblyWorker('Fred', 2, 15.50, 40)
    e3 = Employee('Sean', 3)

    print(e1)
    print(e2)
    print(e3)

if __name__ == '__main__':
    test()
