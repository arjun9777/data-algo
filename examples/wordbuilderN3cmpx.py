#! /usr/bin/env python3

def buildwords(listA: list) -> list:
    collect = []
    for key, value in enumerate(listA):
        print(f"Outer for loop key : {key} and value : {value}")
        for key2, value2 in enumerate(listA):
            print(f"************* Inner for loop key : {key2} and value : {value2}")
            for key3, value3 in enumerate(listA):
                print(f"---------------------------- Third for loop key : {key3} and value : {value3}")
                if (key != key2 & key2 !=key3 & key != key3):
                    collect.append(value+value2+value3)
    return collect

a = ["a", "b", "c", "d"]
x = buildwords(a)
print(f"Combination of two characters strings : {x}")

#Note : This algo has O(N^3) complexity. Not counting print statement as it is for understanding complexity 