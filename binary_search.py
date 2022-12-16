#!/usr/bin/env python3

list_a = [2,5,6,9,10,15,16,18,20,21,22,30]



def binary_search(ordered_list, search_value):
    lower_bound = 0
    upperbound = len(ordered_list) - 1

    while lower_bound <= upperbound:
        midpoint = int((upperbound  + lower_bound) / 2) 
        #print(midpoint)

        value_at_midpoint = ordered_list[midpoint]
        #print(value_at_midpoint)

        if search_value == value_at_midpoint:
            return midpoint
        elif search_value < value_at_midpoint:
            upperbound = midpoint - 1
        elif search_value > value_at_midpoint:
            lower_bound = midpoint + 1
        else:
            print(f"Cannot find value {search_value}")

list_b = [3, 17,75, 80, 202]
print(binary_search(list_a, 22))



