#! /usr/bin/env python3

def double_array(array : list, index = 0):
    if index >= len(array):
        return
    array[index] *= 2     
    double_array(array, index + 1)

a = [1,2,3,4]
double_array(a)
print(f"Doubling values of the array : {a}")