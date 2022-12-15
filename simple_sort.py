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

print(bubble_sort([5,5,9,1,8,2]))





