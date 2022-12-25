#! /usr/bin/env python3


def intersaction(listA, listB):
    intersact = []
    for key, value in enumerate(listA):
        print(f"Outer for loop index : {key} and value : {value}")
        for key2, value2 in enumerate(listB):
            print(f"************Inner for loop index : {key2} and value : {value2}")
            if value == value2:
                intersact.append(value)
                break #if condition matches, break the inner for loop as there is no point of iterating any more
    return intersact

first_array = [2,8,1]
second_array = [5,8,3]

x = intersaction(first_array, second_array)
print(x)

