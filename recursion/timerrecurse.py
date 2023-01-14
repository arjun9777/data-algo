#! /usr/bin/env python3

import time

def timerrec(nume: int):
    print(nume)
    time.sleep(1)
    if (nume == 1):
        return
    else:
        timerrec(nume - 1)
timerrec(10)


