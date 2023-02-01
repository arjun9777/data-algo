#! /usr/bin/env python3
from termcolor import colored

listB = []

def evennumber(listA: list) -> list:
    if len(listA) == 0:
        return []

    if listA[0] % 2 == 0:
        listB.append(listA[0])

    evennumber(listA[1:])

    return listB


if (__name__ == "__main__"):
    a = [0,12,13,14,15,16]
    x = evennumber(a)
    print(colored(f"List of even number : {x}", 'green'))
