#! /usr/bin/env python3

def stringreversal(stringany: str) -> str:
    if len(stringany) == 1:
        return stringany[0]
    print(f"Each recursive call on string : {stringany}")
    return stringreversal(stringany[1:len(stringany)]) + stringany[0]

a = "abcde"
x = stringreversal(a)
print(f"Input string is : {a!r} \nOutput string is : {x!r}")
