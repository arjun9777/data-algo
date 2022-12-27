#! /usr/bin/env python3


def buildwords(listA: list) -> list:
    collect = []
    for key, value in enumerate(listA):
        print(f"Outer for loop key : {key} and value : {value}")
        for key2, value2 in enumerate(listA):
            print(f"************* Inner for loop key : {key2} and value : {value2}")
            if key != key2:
                collect.append(value+value2)
    return collect

a = ["a", "b", "c", "d"]
x = buildwords(a)
print(f"Combination of two characters strings {x}")
