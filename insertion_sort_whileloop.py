#! /usr/bin/env python3

def insertion_sort(listA):
    for i in range(1, len(listA)):
        print(f"Pass-through : {i} and value sorting : {listA[i]}")

        temp_value = listA[i]
        position = i - 1 # Keeping track of position Max value we like to work with 
        print(f"Before performing any operations at position : {position}")

        while position >= 0:
            if listA[position] > temp_value:
                listA[position + 1] = listA[position]
                position -=1
            else:
                break
        
        print(f"Deciding the right position after while loop : {position + 1}")
        listA[position + 1] = temp_value
    return listA

x = insertion_sort([4,2,7,1,3,9,1,56])
print(x)



