#! /usr/bin/env python3

def number_of_paths(n: int) -> int:
    if n < 0 :
        return 0
    if n ==1 or n == 0:
        return 1
    return number_of_paths(n - 1) + number_of_paths(n - 2) + number_of_paths(n - 3)

a = 10
x = number_of_paths(a)
print(f"Total number of paths : {x} for input number : {a}")

    
