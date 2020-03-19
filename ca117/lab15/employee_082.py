#!/usr/bin/env python3

class Employee(object):

    next_employee_number = 0

    def __init__(self, name, employee_num=next_employee_number, hours_worked=0, hourly_rate=9.25):
        
        self.name = name
        self.employee_num = Employee.next_employee_number
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.wages = self.hourly_rate * self.hours_worked

        Employee.next_employee_number += 1

    def __str__(self):
        n = "Name: {}".format(self.name)
        e_id = "ID: {}".format(self.employee_num)
        hrs = "Hours: {:.2f}".format(self.hours_worked)
        rate = "Rate: {:.2f}".format(self.hourly_rate)
        wages = "Wages: {:.2f}".format(self.wages)

        return "\n".join([n, e_id, hrs, rate, wages])

    def add_hours(self, hours):
        self.hours_worked += hours
        self.wages = self.hourly_rate * self.hours_worked
