#! /usr/bin/env python3

def double_array(array, index):
    if index >= len(array):
        return
    array[index] *= 2     
    double_array(array, index + 1)

a = [1,2,3,4]
double_array(a, 0)
print(f"Doubling values of the array : {a}")