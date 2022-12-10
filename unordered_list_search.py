#! /usr/bin/python3
def linear_search(list_of_elements, search_value):
    for key, value in enumerate(list_of_elements):
        print(f"Iterating index: {key} and value: {value}")
        if value == search_value:
            print(f"Found value at index: {key} and value: {value}")
            break
    print("Out of for loop") 

linear_search([17,3,75,202,80], 3)


