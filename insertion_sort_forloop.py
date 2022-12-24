#! /usr/bin/env python3

#This is insertion sort using For loop. 
#It does use range in-built function called reverse. Can be avoided using while loop

def insertion_sort(list_a):
    for i in range(1, len(list_a)):
        temp_value = list_a[i]
        print(f"Working for a value in array {temp_value!r}")
        for j in reversed(range(i)):
            print (f"Index {j} and value {list_a[j]}")
            if list_a[j] > temp_value:
                list_a[j + 1] = list_a[j]
                list_a[j] = temp_value 
    return list_a


x = insertion_sort([4,2,7,1,3,9,1,56])
print(f"At the end sorted array : {x}")


