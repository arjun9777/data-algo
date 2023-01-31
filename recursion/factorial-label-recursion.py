#! /usr/bin/env python3
# We want to print, For instance, 5x4x3x2x1=120 (label = factorial value)

def factorial_label(label, n):
    if n == 0:
        return [label + "=", 1]
    else:
        if label == "":
            new_label = str(n)
        else:
            new_label = label + "x" + str(n)
        data = factorial_label(new_label, n-1)
        # Next line is for calculating actual factorial value
        ret_value = [data[0], n * data[1]]
        return ret_value


if __name__ == "__main__":
    output = factorial_label("", 5)
    print(output[0] + str(output[1]))


