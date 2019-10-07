#!/usr/bin/env python3

def remove_adjacent(lst):
    res = []

    for x in lst:
        if len(res) == 0 or res[-1] != x:
            res.append(x)

    return res


def linear_merge(lst1, lst2):
    res = []
    j = 0

    for i in range(0, len(lst1)):
        while j < len(lst2) and lst2[j] < lst1[i]:
            res.append(lst2[j])
            j += 1
        res.append(lst1[i])

    for i in range(j, len(lst2)):
        res.append(lst2[i])

    return res

