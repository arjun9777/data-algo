#! /usr/bin/env python3

import time

def timer(number : int) -> int:
    for i in reversed(range(number)):
        print(i + 1)
        time.sleep(1)
    return "Launch"
x = timer(10)
print(f"{x}")
