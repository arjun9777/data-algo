#! /usr/bin/env python3
from colorama import Fore, Back, Style
from termcolor import colored


def anagram(st):
    print(colored(f"Value of st variable : {st}", 'green'))
    if st == '':
        return ['']

    lout = [ ]

    for i in range(len(st)):
        #print(f"Value of outter for loop index : {i} **********{st[i]}")
        st2 = st[:i]+st[i+1:]
        #print(st2)
        lout2 = anagram(st2)
        print(colored(f"------------------Value of lout2 variable : {lout2}", 'yellow'))
        for w in lout2:
            print(colored(f"Value of variable w : {w}", 'red'))
            lout.append(st[i]+w)
            print(f"values in lout variable : {lout}")

    return lout

a = "abcd"
x = anagram(a)
print(x)
