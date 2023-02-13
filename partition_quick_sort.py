#! /usr/bin/env python3

def partition(ListA:list, left_pointer: int= 0, rigth_pointer: int=0) -> list:
    pivot_index = len(ListA) - 1

    pivot = ListA[pivot_index]

    right_pointer = len(ListA) - 2

    while True:
        while ListA[left_pointer] < pivot:
            left_pointer = left_pointer + 1
        while ListA[right_pointer] > pivot:
            right_pointer = right_pointer - 1

        if left_pointer >= right_pointer:
            break
        else:
            ListA[left_pointer], ListA[right_pointer] = ListA[right_pointer], ListA[left_pointer]
            left_pointer = left_pointer + 1

    ListA[left_pointer], ListA[pivot_index] = ListA[pivot_index], ListA[left_pointer]

    return ListA


a = [0,5,2,1,6,3]
x = partition(a)

print(f"{x}")

