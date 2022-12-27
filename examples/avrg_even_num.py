#! /usr/bin/env python3

def average_even_numbers(listA : list):
    sum = 0
    count_of_event_number = 0
    for key, value in enumerate(listA):
        print(f"Iterating for loop key : {key} and value : {value} ")
        if abs(value) % 2 == 0:
            sum += abs(value)
            count_of_event_number += 1
    return sum / count_of_event_number


a = [1,2,3,-4,5,-6,7,-8,9,10]
x = average_even_numbers(a)
print(f"Average mean of even numbers : {x}")
