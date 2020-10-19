#!/usr/bin/env python3

def set_intersection(s1, s2):
    return s1.intersection(s2)

def set_stuff(s1, s2):
    is_subset, is_superset, union = s1.issubset(s2), s1.issuperset(s2), s1.union(s2)

    return (union, is_subset, is_superset)

def unique_list(lst):
    uq_list = list(set(lst))

    return uq_list
