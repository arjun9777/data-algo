#! /usr/bin/env python3

def intersactiontwolist(listA: list, listB:list) -> list:
    intersact = []

    if len(listA) > len(listB):
        largerlist = listA
        smallerlist = listB
    else:
        largerlist = listB
        smallerlist = listA
    
    largervalues = {}

    for key, value in enumerate(largerlist):
        largervalues[value] = True

    for key2, item in enumerate(smallerlist):
        try:
            if largervalues[item]:
                intersact.append(item)
        except KeyError:
            pass
    return intersact

a = [1,2,3,4]
b = [0,1,2,4,6,8]

x = intersactiontwolist(a, b)
print(f"Intersaction of two lists : {x}")