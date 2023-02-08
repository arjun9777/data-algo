#! /usr/bin/env python3


def totalcharacter(listA:list)->int:

    if len(listA) == 0:
        return 0
    else:
        return len(listA[0]) + totalcharacter(listA[1:])


a = ["ab", "c", "def", "ghij"]

x = totalcharacter(a)

print(f"Total number of characters in list of strings : {x}")
