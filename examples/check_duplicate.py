#! /usr/bin/evn python3
#Need to think again


def find_duplicate_old(list_z):
    list_appear = []
    for i in range(len(list_z)):
        if list_z[i] < len(list_z):
            print(list_z[i])
            if list_z[(list_z[i])] < 0:
                #print(list_z[i])
                list_appear.append(list_z[list_z[i]])
            else:
                list_z[list_z[i]] = list_z[list_z[i]] * -1
                #print(list_z[i])
        else:
            for j in range(len(list_z), list_z[i] + 1):
                list_z.insert(j,1)
            #print(list_z)
            list_z[list_z[i]] = list_z[list_z[i]] * -1
            #print(list_z)
    return list_appear

print(find_duplicate_old([3,2,1,2,8]))