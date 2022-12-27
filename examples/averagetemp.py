#! /usr/bin/env python3

def average_temp_celsius(listA: list) -> int:

    total_item = len(listA)
    sum = 0
    for key, value in enumerate(listA):
        print(f"For loop index : {key} and value : {value}")
        celsius = (value - 32)/1.8
        sum +=celsius
    return int(sum/total_item)


a = [27,36,41,44,42,40,38]
x = average_temp_celsius(a)
print(f"Average temperature in celsius : {x}")