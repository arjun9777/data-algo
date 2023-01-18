#! /usr/bin/env python3

def factorial(number : int) -> int:
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

a = 5
x = factorial(a)
print(f"Factorial of number {a} is : {x}")
