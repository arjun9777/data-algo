#! /usr/bin/env python3

def bubble_sort(list_a):
    unsorted_index_upto = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_index_upto):
            if list_a[i] > list_a [i + 1]:
                list_a[i] , list_a[i + 1] = list_a[i + 1], list_a[i]
                sorted = False
        unsorted_index_upto -= 1
    return list_a


print(bubble_sort([9,1,5,8,7,2,1,5,5,6,8,15,3,9,19,18,88,10,1,100,4,8]))