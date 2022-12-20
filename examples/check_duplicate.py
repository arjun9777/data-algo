#! /usr/bin/evn python3

"""
#This solution is O(N^2) time complexity.  
def hasduplicatevalue(list_a):
    #steps = 0
    for i in range(len(list_a)):
        for j in range(len(list_a)):
            #steps += 1
            if (i != j and list_a[i] == list_a[j]):
                return True
    return False      #To print number of steps algo takes, replace False with steps variable and uncomment steps
"""

#This is O(N) time complexity instead of O(N^2)

"""
def hasduplicatevalueON(list_a):
    existingNumber = []

    for i in list_a:
        m = abs(i)
        #print(list_a[m-1])

        if list_a[m-1] < 0:
            existingNumber.append(m)
        else:
            list_a[m-1] *= -1
    return existingNumber

print(hasduplicatevalueON([4,3,2,7,8,2,3,1,13]))

"""

"""
# Python3 code to find duplicates in O(n) time
#numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1]
numRay = [4,3,2,7,8,2,3,1,13]
arr_size = len(numRay)
for i in range(arr_size):
 
    x = numRay[i] % arr_size
    print(x)
    #numRay[x] = numRay[x] + arr_size

"""

"""

print("The repeating elements are : ")
for i in range(arr_size):
    if (numRay[i] >= arr_size*2):
        print(i, " ")
"""
#I need to think on this algorithm

def find_duplicate_old(list_z):
    list_appear = []
    for i in range(len(list_z)):
        if list_z[i] < len(list_z):
            if list_z[i] < 0:
                #list_appear.append(list_z[i])
                return True
            else:
                list_z[i-1] *= -1
        else:
            for y in range(len(list_z), list_z[i]):
                print(y)
                list_z.insert(y,1)
            if list_z[i] < 0:
                #list_appear.append(list_z[i - 1])
                return True
            else:
                list_z[i] *= -1
    return list_appear
print(find_duplicate_old([4,2,7,8,3,1,13]))