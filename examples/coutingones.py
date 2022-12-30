#! /usr/bin/env python3

def count_one(outer_array):
    count = 0
    for key, inner_array in enumerate(outer_array):
        print(f"Outer loop key : {key} and value : {inner_array}")
        for key1, number in enumerate(inner_array):
            print(f"----------------Inner loop key : {key1} and value : {number}")
            if number == 1:
                count +=1
    return count

a = [ [0, 1, 1, 1, 0],[0, 1, 0, 1, 0, 1],[1, 0]]

x = count_one(a)
print(f"How many 1's are there in array of arrays : {x}")
