#! /usr/bin/env python3
from termcolor import colored


def partition(ListA:list, left_pointer:int, right_pointer:int) -> int:
    pivot_index = right_pointer

    pivot = ListA[pivot_index]

    right_pointer = len(ListA) - 2

    while True:
        while ListA[left_pointer] < pivot:
            #print(f"Left pointer value {ListA[left_pointer]}")
            left_pointer = left_pointer + 1
        while ListA[right_pointer] > pivot:
            #print(f"Right pointer value {ListA[right_pointer]}")
            right_pointer = right_pointer - 1

        if left_pointer >= right_pointer:
            #print(f"IF statement : left value {ListA[left_pointer]}, right value {ListA[right_pointer]}")
            break
        else:
            ListA[left_pointer], ListA[right_pointer] = ListA[right_pointer], ListA[left_pointer]
            #print(f"----------------------------left pointer value :{ListA[left_pointer]} and right pointer value {ListA[right_pointer]}")
            left_pointer = left_pointer + 1 #We only increase left pointer index but right pointer is still there where it was
            #print(ListA)

    ListA[left_pointer], ListA[pivot_index] = ListA[pivot_index], ListA[left_pointer] #Finally swap the pivot with the value that the left pointer is pointing to beacuase 
    # left pointer value is greater than the pivot value
    #print(colored(f"*******************************************left pointer value :{ListA[left_pointer]} and right pointer value {ListA[right_pointer]}", "yellow"))

    return left_pointer


def quicksort(ListB, left_index: int, right_index: int): 
    if left_index < right_index:
        #Parition the range of elements and grab the index of the pivot
        pivot_index = partition(ListB, left_index, right_index)
        #Recursively call this quicksort method on whatever is to the left of the pivot
        quicksort(ListB, left_index, pivot_index - 1)
        #Recursively call this quicksort method on whatever is on the right of the pivot
        quicksort(ListB, pivot_index + 1,right_index)
    return ListB

a = [0,5,2,1,6,3]
#a = [1, 7, 4, 1, 10, 9, -2]
x = quicksort(a, 0, len(a) - 1)

print(colored(f"Quicksort output is : {x}", "green"))

