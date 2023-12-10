#! /usr/bin/python3

def linear_search(list_of_element, search_number)
    for key, value in enumerate(list_of_element):
        print(f"search for element at index {key} and value {value}")
        if value == search_number:
            print(f"found match at index {key} and {value}")
            break
        elif (value > search_number):
            break
    print ("out of for loop")

linear_search([3,17,75,80,202], 22)


