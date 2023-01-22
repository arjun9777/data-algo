#! /usr/bin/env python3

def count_character(stringvalue: str) -> str:
    if len(stringvalue) == 0:
        return 0

    if stringvalue[0] == "x":
        print(f"Running for IF statement : {stringvalue}")
        return 1 + count_character(stringvalue[1:len(stringvalue)])
    else:
        print(f"-------------------------Running for ELSE statement : {stringvalue}") 
        return count_character(stringvalue[1:len(stringvalue)]) 


a = "axbxcxd"
b = 'a'

x = count_character(a)

print(x)