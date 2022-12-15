#! /usr/bin/env python3

def bubble_sort(list_b:list) -> list:

    for key in range(len(list_b)):
        #print(f"key --- {key} and value ----- {list_b[key]}")
        for i in range(key+1, len(list_b)):
            #print(f"Inner key -------- {i} and value -------- {list_b[i]}")
            if list_b[key] > list_b[i]:
                temp = list_b[key]
                list_b[key] = list_b[i]
                list_b[i] = temp
    return list_b

print(bubble_sort([9,1,5,8,7,2,1,5,5,6,8,15,3,9,19,18,88,10,1,100,4,8]))





