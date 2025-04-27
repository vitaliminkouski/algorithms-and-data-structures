import numpy as np


def is_binary_heap(arr, arr_len):
    medium = arr_len // 2 - 1
    for i in range(medium, -1, -1):
        left_son = 2 * i + 1
        right_son = 2 * i + 2
        if ((left_son < arr_len and arr[left_son] < arr[i]) or
                (right_son < arr_len and arr[2 * i + 2] < arr[i])):
            return False

    return True


with open("input.txt", "r") as f:
    arr_len = int(f.readline())
    arr = np.fromstring(f.readline(), sep=" ", dtype="int")

with open("output.txt", "w") as f:
    if (is_binary_heap(arr, arr_len)):
        f.write("Yes")
    else:
        f.write("No")
