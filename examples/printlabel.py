#! /usr/bin/env python3

def count_inventory(listA: list) -> list:
    clothing_options = []
    for item in listA:
        for i in range(1,6):
            clothing_options.append(f"{item}, size: {i}")
    return clothing_options

a = ["Purple Shirt", "Green Shirt"]
x = count_inventory(a)
print(x)

