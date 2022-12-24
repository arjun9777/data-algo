#! /usr/bin/env python3


def selection_sort_cmplx(list_a):
    for i in range(len(list_a) - 1):
        print(f"Iterating for {i} and value {list_a[i]}")
        lowestNumberIndex = i
        for j in range(i+1, len(list_a)):
            print(f"Inner for loop iteration {j} and Value : {list_a[j]}")
            if list_a[j] < list_a[lowestNumberIndex]:
                lowestNumberIndex = j
    
        if lowestNumberIndex != i:
            temp = list_a[i]
            list_a[i] = list_a[lowestNumberIndex]
            list_a[lowestNumberIndex] = temp
    
    return list_a

x = selection_sort_cmplx([4,2,7,1,3])
print(x)