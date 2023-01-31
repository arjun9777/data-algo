#! /usr/bin/env python3

def permute(str, remaining, final_set):
    #abc => abc, acb, bac, bca, cab, cba
    if(remaining == ""):
        final_set.add(str)
    for c in remaining: 
        print(f"FOR loop value : {c}")
        new_str = str + c 
        print(f"new_str variable value : {new_str}")
        index = remaining.index(c)
        print(f"-------------------index {c!r}: {index}")
        print(f"two important values first : {remaining[0:index:]} and second value : {remaining[index + 1::]}")
        new_remaining = remaining[0:index:] + remaining[index+1::]
        print("**********************************************************************************************************************")
        permute(new_str, new_remaining, final_set)
    

if (__name__ == "__main__"):
    final_set = set()
    permute("", "abc", final_set)
    for s in final_set:
        print(s)





